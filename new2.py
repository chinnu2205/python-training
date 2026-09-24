import csv
import os
from datetime import date, datetime

FILE = "drugs.csv"


class PharmaSystem:

    def __init__(self):
        if not os.path.exists(FILE):
            with open(FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Quantity", "Price", "Expiry"])


    # 1. Add Drug
    def add_drug(self):
        drug_id = input("Enter Drug ID: ")
        name = input("Enter Drug Name: ")

        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        expiry = input("Enter Expiry Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(expiry, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format.")
            return

        # Check duplicate ID
        with open(FILE, "r") as f:
            for row in csv.DictReader(f):
                if row["ID"] == drug_id:
                    print("Drug ID already exists.")
                    return

        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([drug_id, name, quantity, price, expiry])

        print("Drug added successfully!")


    # 2. Display Drugs
    def display_drugs(self):
        with open(FILE, "r") as f:
            drugs = list(csv.DictReader(f))

        if not drugs:
            print("No drugs available.")
            return

        print("\n========== DRUG DETAILS ==========")

        for drug in drugs:
            print("ID       :", drug["ID"])
            print("Name     :", drug["Name"])
            print("Quantity :", drug["Quantity"])
            print("Price    : ₹", drug["Price"])
            print("Expiry   :", drug["Expiry"])
            print("--------------------------------")


    # 3. Search Drug
    def search_drug(self):
        drug_id = input("Enter Drug ID: ")

        with open(FILE, "r") as f:
            for drug in csv.DictReader(f):
                if drug["ID"] == drug_id:
                    print("\nDrug Found!")
                    print("ID       :", drug["ID"])
                    print("Name     :", drug["Name"])
                    print("Quantity :", drug["Quantity"])
                    print("Price    : ₹", drug["Price"])
                    print("Expiry   :", drug["Expiry"])
                    return

        print("Drug not found.")


    # 4. Update Quantity
    def update_quantity(self):
        drug_id = input("Enter Drug ID: ")

        try:
            new_quantity = int(input("Enter New Quantity: "))
        except ValueError:
            print("Enter a valid quantity.")
            return

        rows = []
        found = False

        with open(FILE, "r") as f:
            reader = csv.DictReader(f)

            for drug in reader:
                if drug["ID"] == drug_id:
                    drug["Quantity"] = str(new_quantity)
                    found = True

                rows.append(drug)

        if found:
            with open(FILE, "w", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=["ID", "Name", "Quantity", "Price", "Expiry"]
                )
                writer.writeheader()
                writer.writerows(rows)

            print("Quantity updated successfully!")
        else:
            print("Drug not found.")


    # 5. Check Expired Drugs
    def check_expiry(self):
        today = date.today()
        found = False

        print("\n========== EXPIRED DRUGS ==========")

        with open(FILE, "r") as f:
            for drug in csv.DictReader(f):
                expiry = datetime.strptime(
                    drug["Expiry"], "%d-%m-%Y"
                ).date()

                if expiry < today:
                    print("ID     :", drug["ID"])
                    print("Name   :", drug["Name"])
                    print("Expiry :", drug["Expiry"])
                    print("--------------------------------")
                    found = True

        if not found:
            print("No expired drugs found.")


    # 6. Delete Drug
    def delete_drug(self):
        drug_id = input("Enter Drug ID: ")

        rows = []
        found = False

        with open(FILE, "r") as f:
            reader = csv.DictReader(f)

            for drug in reader:
                if drug["ID"] == drug_id:
                    found = True
                else:
                    rows.append(drug)

        if found:
            with open(FILE, "w", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=["ID", "Name", "Quantity", "Price", "Expiry"]
                )
                writer.writeheader()
                writer.writerows(rows)

            print("Drug deleted successfully!")
        else:
            print("Drug not found.")


    # 7. Total Stock Value
    def total_stock_value(self):
        total = 0

        with open(FILE, "r") as f:
            for drug in csv.DictReader(f):
                total += int(drug["Quantity"]) * float(drug["Price"])

        print("Total Stock Value: ₹", round(total, 2))


# Main Program

pharma = PharmaSystem()

while True:

    print("\n===== PHARMA DRUG MANAGEMENT SYSTEM =====")
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
        pharma.add_drug()

    elif choice == "2":
        pharma.display_drugs()

    elif choice == "3":
        pharma.search_drug()

    elif choice == "4":
        pharma.update_quantity()

    elif choice == "5":
        pharma.check_expiry()

    elif choice == "6":
        pharma.delete_drug()

    elif choice == "7":
        pharma.total_stock_value()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")