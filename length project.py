
import csv
import os
from datetime import date, datetime


# Store CSV file in the same folder as this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRUGS_FILE = os.path.join(BASE_DIR, "drugs.csv")


class Drug:

    def __init__(
        self,
        drug_id,
        drug_name,
        quantity,
        price,
        expiry_date
    ):
        self.drug_id = drug_id
        self.drug_name = drug_name
        self.quantity = quantity
        self.price = price
        self.expiry_date = expiry_date


class PharmaSystem:

    def __init__(self):
        self.create_file()

    # ----------------------------------------
    # CREATE CSV FILE
    # ----------------------------------------

    def create_file(self):

        if not os.path.exists(DRUGS_FILE):

            with open(
                DRUGS_FILE,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "drug_id",
                    "drug_name",
                    "quantity",
                    "price",
                    "expiry_date"
                ])

    
    # ADD DRUG
    

    def add_drug(self):

        drug_id = input("Enter Drug ID: ").strip()

        if not drug_id:
            print("Drug ID cannot be empty.")
            return

        # Check duplicate Drug ID

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for drug in reader:

                if drug["drug_id"] == drug_id:

                    print("Drug ID already exists.")
                    return

        drug_name = input("Enter Drug Name: ").strip()

        if not drug_name:
            print("Drug name cannot be empty.")
            return

        # Get quantity

        try:

            quantity = int(
                input("Enter Quantity: ")
            )

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:

            print("Enter a valid quantity.")
            return

        # Get price

        try:

            price = float(
                input("Enter Price: ")
            )

            if price < 0:
                print("Price cannot be negative.")
                return

        except ValueError:

            print("Enter a valid price.")
            return

        # Get expiry date

        expiry_date = input(
            "Enter Expiry Date (DD-MM-YYYY): "
        ).strip()

        try:

            datetime.strptime(
                expiry_date,
                "%d-%m-%Y"
            )

        except ValueError:

            print("Invalid date format.")
            return

        # Save drug permanently in CSV

        with open(
            DRUGS_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                drug_id,
                drug_name,
                quantity,
                price,
                expiry_date
            ])

        print("Drug added successfully!")
        print("Drug details saved in drugs.csv")

    
    # DISPLAY DRUGS
    

    def display_drugs(self):

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            drugs = list(reader)

        if not drugs:

            print("No drugs available.")
            return

        print("\n========== DRUG DETAILS ==========")

        for drug in drugs:

            print(
                f"\nDrug ID: {drug['drug_id']}"
            )

            print(
                f"Drug Name: {drug['drug_name']}"
            )

            print(
                f"Quantity: {drug['quantity']}"
            )

            print(
                f"Price: ₹{drug['price']}"
            )

            print(
                f"Expiry Date: {drug['expiry_date']}"
            )

            print("-" * 35)

    # ----------------------------------------
    # SEARCH DRUG
    # ----------------------------------------

    def search_drug(self):

        drug_id = input("Enter Drug ID: ").strip()

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for drug in reader:

                if drug["drug_id"] == drug_id:

                    print("\n===== DRUG FOUND =====")

                    print(
                        f"Drug ID: {drug['drug_id']}"
                    )

                    print(
                        f"Drug Name: {drug['drug_name']}"
                    )

                    print(
                        f"Quantity: {drug['quantity']}"
                    )

                    print(
                        f"Price: ₹{drug['price']}"
                    )

                    print(
                        f"Expiry Date: "
                        f"{drug['expiry_date']}"
                    )

                    return

        print("Drug not found.")

    
    # UPDATE QUANTITY
    

    def update_quantity(self):

        drug_id = input("Enter Drug ID: ").strip()

        try:

            new_quantity = int(
                input("Enter New Quantity: ")
            )

            if new_quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:

            print("Enter a valid quantity.")
            return

        rows = []
        found = False

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            fieldnames = reader.fieldnames

            for drug in reader:

                if drug["drug_id"] == drug_id:

                    drug["quantity"] = str(new_quantity)
                    found = True

                rows.append(drug)

        if found:

            with open(
                DRUGS_FILE,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(rows)

            print("Quantity updated successfully!")

        else:

            print("Drug not found.")


    # CHECK EXPIRED DRUGS
    

    def check_expiry(self):

        today = date.today()
        found = False

        print("\n========== EXPIRED DRUGS ==========")

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for drug in reader:

                expiry = datetime.strptime(
                    drug["expiry_date"],
                    "%d-%m-%Y"
                ).date()

                if expiry < today:

                    print(
                        f"\nDrug ID: {drug['drug_id']}"
                    )

                    print(
                        f"Drug Name: "
                        f"{drug['drug_name']}"
                    )

                    print(
                        f"Expiry Date: "
                        f"{drug['expiry_date']}"
                    )

                    found = True

        if not found:

            print("No expired drugs found.")

    # ----------------------------------------
    # DELETE DRUG
    # ----------------------------------------

    def delete_drug(self):

        drug_id = input("Enter Drug ID: ").strip()

        rows = []
        found = False

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            fieldnames = reader.fieldnames

            for drug in reader:

                if drug["drug_id"] == drug_id:

                    found = True

                else:

                    rows.append(drug)

        if found:

            with open(
                DRUGS_FILE,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(rows)

            print("Drug deleted successfully!")

        else:

            print("Drug not found.")

    # ----------------------------------------
    # TOTAL STOCK VALUE
    # ----------------------------------------

    def total_stock_value(self):

        total = 0

        with open(
            DRUGS_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for drug in reader:

                quantity = int(
                    drug["quantity"]
                )

                price = float(
                    drug["price"]
                )

                total = total + (
                    quantity * price
                )

        print(
            f"\nTotal Stock Value: ₹{total:.2f}"
        )


# ============================================
# MAIN PROGRAM
# ============================================

pharma_system = PharmaSystem()


while True:

    print("\n")

    print(
        "===== PHARMA DRUG MANAGEMENT SYSTEM ====="
    )

    print("1. Add Drug")
    print("2. Display Drugs")
    print("3. Search Drug")
    print("4. Update Quantity")
    print("5. Check Expired Drugs")
    print("6. Delete Drug")
    print("7. Total Stock Value")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        pharma_system.add_drug()

    elif choice == "2":

        pharma_system.display_drugs()

    elif choice == "3":

        pharma_system.search_drug()

    elif choice == "4":

        pharma_system.update_quantity()

    elif choice == "5":

        pharma_system.check_expiry()

    elif choice == "6":

        pharma_system.delete_drug()

    elif choice == "7":

        pharma_system.total_stock_value()

    elif choice == "8":

        print("Thank you for using Pharma Drug Management System!")
        break

    else:

        print("Invalid choice.")