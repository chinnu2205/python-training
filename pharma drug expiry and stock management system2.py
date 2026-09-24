import csv
import os
from datetime import date, datetime

FILE = "drugs.csv"


class PharmaSystem:

    def __init__(self):
        if not os.path.exists(FILE):
            with open(FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["drug_id", "drug_name", "quantity", "price", "expiry_date"]
                )

    # ADD DRUG
    def add_drug(self):
        drug_id = input("Enter Drug ID: ")
        drug_name = input("Enter Drug Name: ")

        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
        except ValueError:
            print("Enter valid quantity and price.")
            return

        expiry_date = input("Enter Expiry Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(expiry_date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format.")
            return

        # Check duplicate ID
        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for drug in reader:
                if drug["drug_id"] == drug_id:
                    print("Drug ID already exists.")
                    return

        # Save drug
        with open(FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [drug_id, drug_name, quantity, price, expiry_date]
            )

        print("Drug added successfully!")


    # DISPLAY DRUGS
    def display_drugs(self):
        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            drugs = list(reader)

        if len(drugs) == 0:
            print("No drugs available.")
            return

        print("\n========== DRUG DETAILS ==========")

        for drug in drugs:
            print("Drug ID      :", drug["drug_id"])
            print("Drug Name    :", drug["drug_name"])
            print("Quantity     :", drug["quantity"])
            print("Price        : ₹", drug["price"])
            print("Expiry Date  :", drug["expiry_date"])
            print("---------------------------------")


    # SEARCH DRUG
    def search_drug(self):
        drug_id = input("Enter Drug ID: ")

        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for drug in reader:
                if drug["drug_id"] == drug_id:
                    print("\n========== DRUG FOUND ==========")
                    print("Drug ID      :", drug["drug_id"])
                    print("Drug Name    :", drug["drug_name"])
                    print("Quantity     :", drug["quantity"])
                    print("Price        : ₹", drug["price"])
                    print("Expiry Date  :", drug["expiry_date"])
                    return

        print("Drug not found.")


    # UPDATE QUANTITY
    def update_quantity(self):
        drug_id = input("Enter Drug ID: ")

        try:
            new_quantity = int(input("Enter New Quantity: "))
        except ValueError:
            print("Enter a valid quantity.")
            return

        rows = []
        found = False

        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for drug in reader:
                if drug["drug_id"] == drug_id:
                    drug["quantity"] = str(new_quantity)
                    found = True

                rows.append(drug)

        if found:
            with open(FILE, "w", newline="") as file:
                fieldnames = [
                    "drug_id",
                    "drug_name",
                    "quantity",
                    "price",
                    "expiry_date"
                ]

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

        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for drug in reader:
                expiry = datetime.strptime(
                    drug["expiry_date"],
                    "%d-%m-%Y"
                ).date()

                if expiry < today:
                    print("Drug ID     :", drug["drug_id"])
                    print("Drug Name   :", drug["drug_name"])
                    print("Expiry Date :", drug["expiry_date"])
                    print("---------------------------------")
                    found = True

        if not found:
            print("No expired drugs found.")


    # DELETE DRUG
    def delete_drug(self):
        drug_id = input("Enter Drug ID: ")

        rows = []
        found = False

        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for drug in reader:
                if drug["drug_id"] == drug_id:
                    found = True
                else:
                    rows.append(drug)

        if found:
            with open(FILE, "w", newline="") as file:
                fieldnames = [
                    "drug_id",
                    "drug_name",
                    "quantity",
                    "price",
                    "expiry_date"
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(rows)

            print("Drug deleted successfully!")
        else:
            print("Drug not found.")


    # TOTAL STOCK VALUE
    def total_stock_value(self):
        total = 0

        with open(FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for drug in reader:
                quantity = int(drug["quantity"])
                price = float(drug["price"])

                total = total + (quantity * price)

        print("\nTotal Stock Value: ₹", total)


# MAIN PROGRAM

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