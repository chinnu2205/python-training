import os, sqlite3, csv
from datetime import date, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "pharma_inventory.db")
OLD_CSV = os.path.join(BASE_DIR, "drugs.csv")


class PharmaSystem:
    def __init__(self):
        self.create_database()
        self.migrate_old_csv_if_needed()

    def get_connection(self):
        c = sqlite3.connect(DATABASE)
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA synchronous=FULL")
        c.execute("PRAGMA foreign_keys=ON")
        return c

    def create_database(self):
        with self.get_connection() as c:
            c.execute("""CREATE TABLE IF NOT EXISTS drugs (
                drug_id TEXT PRIMARY KEY, drug_name TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity >= 0),
                price REAL NOT NULL CHECK(price >= 0),
                expiry_date TEXT NOT NULL)""")
            c.commit()

    def migrate_old_csv_if_needed(self):
        if not os.path.exists(OLD_CSV):
            return
        try:
            with self.get_connection() as c:
                if c.execute("SELECT COUNT(*) FROM drugs").fetchone()[0]:
                    return
                with open(OLD_CSV, newline="", encoding="utf-8") as file:
                    for row in csv.DictReader(file):
                        try:
                            drug_id = str(row.get("drug_id", "")).strip().upper()
                            name = str(row.get("drug_name", "")).strip()
                            qty = int(row.get("quantity", 0))
                            price = float(row.get("price", 0))
                            expiry = str(row.get("expiry_date", "")).strip()
                            if not drug_id or not name:
                                continue
                            datetime.strptime(expiry, "%d-%m-%Y")
                            c.execute("""INSERT OR IGNORE INTO drugs
                                (drug_id, drug_name, quantity, price, expiry_date)
                                VALUES (?, ?, ?, ?, ?)""",
                                (drug_id, name, qty, price, expiry))
                        except (ValueError, TypeError):
                            continue
                c.commit()
        except (OSError, UnicodeError):
            pass

    def query(self, sql, args=(), one=False):
        with self.get_connection() as c:
            r = c.execute(sql, args)
            return r.fetchone() if one else r.fetchall()

    def generate_drug_id(self):
        ids = [str(x[0]).strip().upper() for x in self.query("SELECT drug_id FROM drugs")]
        nums = [int(x[4:]) for x in ids if x.startswith("DRUG") and x[4:].isdigit()]
        return f"DRUG{max(nums, default=0) + 1:03d}"

    def add_drug(self):
        drug_id = self.generate_drug_id()
        print("\n========== ADD DRUG ==========")
        print("Drug ID (automatic):", drug_id)
        name = input("Enter Drug Name: ").strip()
        if not name:
            print("Drug name cannot be empty.")
            return
        try:
            qty = int(input("Enter Quantity: "))
            if qty < 0:
                print("Quantity cannot be negative.")
                return
            price = float(input("Enter Price Per Unit: "))
            if price < 0:
                print("Price cannot be negative.")
                return
        except ValueError:
            print("Please enter valid numeric values.")
            return
        expiry = input("Enter Expiry Date (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(expiry, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")
            return
        try:
            with self.get_connection() as c:
                c.execute("""INSERT INTO drugs
                    (drug_id, drug_name, quantity, price, expiry_date)
                    VALUES (?, ?, ?, ?, ?)""",
                    (drug_id, name, qty, price, expiry))
                c.commit()
        except sqlite3.Error as error:
            print("ERROR: Drug was not saved.")
            print("Database error:", error)
            return
        print("\n========================================")
        print("DRUG ADDED AND PERMANENTLY SAVED")
        print("========================================")
        print("Drug ID     :", drug_id)
        print("Drug Name   :", name)
        print("Quantity    :", qty)
        print("Price : ₹", price)
        print("Expiry Date :", expiry)
        print("Database    :", DATABASE)
        self.print_stock_status(qty)

    def display_drugs(self):
        drugs = self.query("""SELECT drug_id, drug_name, quantity, price, expiry_date
                              FROM drugs ORDER BY drug_id""")
        print("\n====================== DRUG DETAILS ======================")
        if not drugs:
            print("No drugs available.")
            print("Database:", DATABASE)
            return
        headers, widths = ["Drug ID", "Drug Name", "Quantity", "Price (₹)", "Expiry Date"], [12, 25, 10, 12, 15]
        sep = "+".join("-" * (w + 2) for w in widths)
        print("+" + sep + "+")
        print("| " + " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers)) + " |")
        print("+" + sep + "+")
        for drug_id, name, qty, price, expiry in drugs:
            vals = [str(drug_id), str(name), str(qty), f"{float(price):.2f}", str(expiry)]
            print("| " + " | ".join(vals[i][:widths[i]].ljust(widths[i]) for i in range(5)) + " |")
        print("+" + sep + "+")
        print("Total saved drugs:", len(drugs))
        

    def search_drug(self):
        drug_id = input("Enter Drug ID: ").strip().upper()
        drug = self.query("""SELECT drug_id, drug_name, quantity, price, expiry_date
                             FROM drugs WHERE UPPER(drug_id) = ?""", (drug_id,), True)
        if not drug:
            print("Drug not found.")
            return
        print("\n========== DRUG FOUND ==========")
        print("Drug ID     :", drug[0])
        print("Drug Name   :", drug[1])
        print("Quantity    :", drug[2])
        print("Price Per Unit    : ₹", drug[3])
        print("Expiry Date :", drug[4])

    def update_quantity(self):
        drug_id = input("Enter Drug ID: ").strip().upper()
        try:
            qty = int(input("Enter New Quantity: "))
            if qty < 0:
                print("Quantity cannot be negative.")
                return
        except ValueError:
            print("Please enter a valid whole number.")
            return
        with self.get_connection() as c:
            drug = c.execute("SELECT drug_name FROM drugs WHERE UPPER(drug_id) = ?", (drug_id,)).fetchone()
            if not drug:
                print("Drug not found.")
                return
            if input(f"Change quantity of {drug[0]} to {qty}? (Y/N): ").strip().upper() != "Y":
                print("No changes made.")
                return
            c.execute("UPDATE drugs SET quantity = ? WHERE UPPER(drug_id) = ?", (qty, drug_id))
            c.commit()
        print("Quantity updated and permanently saved.")
        self.print_stock_status(qty)

    def check_expiry(self):
        print("\n========== EXPIRED DRUGS ==========")
        found = False
        near_found = False
        today = date.today()

        for drug_id, name, expiry_text in self.query(
                "SELECT drug_id, drug_name, expiry_date FROM drugs ORDER BY drug_id"):
            try:
                expiry = datetime.strptime(expiry_text, "%d-%m-%Y").date()
            except ValueError:
                continue

            if expiry < today:
                print("Drug ID     :", drug_id)
                print("Drug Name   :", name)
                print("Expiry Date :", expiry_text)
                print("---------------------------------")
                found = True

        if not found:
            print("No expired drugs found.")

        print("\n========== NEAR EXPIRY DRUGS ==========")
        for drug_id, name, expiry_text in self.query(
                "SELECT drug_id, drug_name, expiry_date FROM drugs ORDER BY drug_id"):
            try:
                expiry = datetime.strptime(expiry_text, "%d-%m-%Y").date()
            except ValueError:
                continue

            if today <= expiry <= today + __import__("datetime").timedelta(days=30):
                print("Drug ID     :", drug_id)
                print("Drug Name   :", name)
                print("Expiry Date :", expiry_text)
                print("STATUS      : NEAR EXPIRY DRUG")
                print("---------------------------------")
                near_found = True

        if not near_found:
            print("No near expiry drugs found.")

    def print_stock_status(self, quantity):
        if quantity < 1:
            print("STOCK STATUS : OUT OF STOCK")
        elif quantity < 50:
            print("STOCK STATUS : LOW STOCK")
        elif quantity <= 100:
            print("STOCK STATUS : NORMAL STOCK")
        else:
            print("STOCK STATUS : STOCK AVAILABLE")

    def check_stock_status(self):
        drugs = self.query("SELECT drug_id, drug_name, quantity FROM drugs ORDER BY drug_id")
        print("\n========== STOCK STATUS & ALERTS ==========")
        if not drugs:
            print("No drugs are available.")
            return
        for drug_id, name, qty in drugs:
            print("\nDrug ID   :", drug_id)
            print("Drug Name :", name)
            print("Quantity  :", qty)
            self.print_stock_status(qty)
            if qty < 1:
                print("ALERT : This drug is out of stock.")
            elif qty < 50:
                print("ALERT : Stock quantity is going low.")
            else:
                print("MESSAGE : Sufficient stock is available.")
            print("------------------------------------------")

    def delete_drug(self):
        drug_id = input("Enter Drug ID to delete: ").strip().upper()
        with self.get_connection() as c:
            drug = c.execute("SELECT drug_name FROM drugs WHERE UPPER(drug_id) = ?", (drug_id,)).fetchone()
            if not drug:
                print("Drug not found.")
                return
            print("Drug:", drug[0])
            if input("WARNING: This permanently deletes the record. Type DELETE to confirm: ").strip() != "DELETE":
                print("No changes made. Drug is safe.")
                return
            c.execute("DELETE FROM drugs WHERE UPPER(drug_id) = ?", (drug_id,))
            c.commit()
        print("Drug deleted permanently.")

    def total_stock_value(self):
        total = self.query("SELECT COALESCE(SUM(quantity * price), 0) FROM drugs", one=True)[0]
        print("\nTotal Stock Value: ₹", round(total, 2))


pharma = PharmaSystem()

while True:
    print("\n===== PHARMA DRUG MANAGEMENT SYSTEM =====")
    for i, item in enumerate(["Add Drug", "Display Drugs", "Search Drug", "Update Quantity",
                              "Check Expired Drugs", "Delete Drug", "Total Stock Value",
                              "Check Stock Status & Alerts", "Exit"], 1):
        print(f"{i}. {item}")
    choice = input("Enter your choice: ").strip()
    actions = {
        "1": pharma.add_drug, "2": pharma.display_drugs, "3": pharma.search_drug,
        "4": pharma.update_quantity, "5": pharma.check_expiry, "6": pharma.delete_drug,
        "7": pharma.total_stock_value, "8": pharma.check_stock_status
    }
    if choice in actions:
        actions[choice]()
    elif choice == "9":
        print("Data has already been permanently saved.")
        print("Database:", DATABASE)
        print("Thank you for using the Pharma Drug Management System!")
        break
    else:
        print("Invalid choice. Please select an option from 1 to 9.")
