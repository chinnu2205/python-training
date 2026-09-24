import csv
import os
from datetime import datetime, date


FILE = "drugs.csv"


class Drug:

    def __init__(self, drug_id, name, quantity, price, expiry):
        self.drug_id = drug_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.expiry = expiry


class PharmaSystem:

    def __init__(self):
        self.create_file()

    # Create CSV file
    def create_file(self):

        if not os.path.exists(FILE):

            with open(FILE, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Drug ID",
                    "Drug Name",
                    "Quantity",
                    "Price",
                    "Expiry Date"
                ])

    # Add Drug
    def add_drug(self):

        drug_id = input("Enter Drug ID: ")

        # Check existing ID
        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["Drug ID"] == drug_id:

                    print("Drug ID already exists!")
                    return

        drug_name = input("Enter Drug Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        expiry = input("Enter Expiry Date (DD-MM-YYYY): ")

        # Check date
        try:
            datetime.strptime(expiry, "%d-%m-%Y")

        except ValueError:
            print("Invalid date format!")
            return

        # Create drug object
        drug = Drug(
            drug_id,
            drug_name,
            quantity,
            price,
            expiry
        )

        # Store data
        with open(FILE, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                drug.drug_id,
                drug.name,
                drug.quantity,
                drug.price,
                drug.expiry
            ])

        print("Drug added successfully!")
        print("Drug details saved successfully!")

    # Display Drugs
    def display_drugs(self):

        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            drugs = list(reader)

        if len(drugs) == 0:

            print("No drugs available.")
            return

        print("\n========== DRUG DETAILS ==========")

        for drug in drugs:

            print("\nDrug ID:", drug["Drug ID"])
            print("Drug Name:", drug["Drug Name"])
            print("Quantity:", drug["Quantity"])
            print("Price: ₹", drug["Price"])
            print("Expiry Date:", drug["Expiry Date"])

            print("-" * 35)

    # Search Drug
    def search_drug(self):

        drug_id = input("Enter Drug ID: ")

        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            for drug in reader:

                if drug["Drug ID"] == drug_id:

                    print("\n===== DRUG FOUND =====")

                    print("Drug ID:", drug["Drug ID"])
                    print("Drug Name:", drug["Drug Name"])
                    print("Quantity:", drug["Quantity"])
                    print("Price: ₹", drug["Price"])
                    print("Expiry Date:", drug["Expiry Date"])

                    return

        print("Drug not found!")

    # Update Quantity
    def update_quantity(self):

        drug_id = input("Enter Drug ID: ")
        new_quantity = input("Enter New Quantity: ")

        rows = []
        found = False

        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            for drug in reader:

                if drug["Drug ID"] == drug_id:

                    drug["Quantity"] = new_quantity
                    found = True

                rows.append(drug)

        if found:

            with open(FILE, "w", newline="") as file:

                fieldnames = [
                    "Drug ID",
                    "Drug Name",
                    "Quantity",
                    "Price",
                    "Expiry Date"
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(rows)

            print("Quantity updated successfully!")

        else:

            print("Drug not found!")

    # Check Expiry
    def check_expiry(self):

        today = date.today()
        found = False

        print("\n========== EXPIRED DRUGS ==========")

        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            for drug in reader:

                expiry = datetime.strptime(
                    drug["Expiry Date"],
                    "%d-%m-%Y"
                ).date()

                if expiry < today:

                    print(
                        "\nDrug ID:",
                        drug["Drug ID"]
                    )

                    print(
                        "Drug Name:",
                        drug["Drug Name"]
                    )

                    print(
                        "Expiry Date:",
                        drug["Expiry Date"]
                    )

                    found = True

        if found == False:

            print("No expired drugs found!")

    # Delete Drug
    def delete_drug(self):

        drug_id = input("Enter Drug ID: ")

        rows = []
        found = False

        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            for drug in reader:

                if drug["Drug ID"] == drug_id:

                    found = True

                else:

                    rows.append(drug)

        if found:

            with open(FILE, "w", newline="") as file:

                fieldnames = [
                    "Drug ID",
                    "Drug Name",
                    "Quantity",
                    "Price",
                    "Expiry Date"
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames
                )

                writer.writeheader()
                writer.writerows(rows)

            print("Drug deleted successfully!")

        else:

            print("Drug not found!")

    # Total Stock Value
    def total_stock_value(self):

        total = 0

        with open(FILE, "r") as file:

            reader = csv.DictReader(file)

            for drug in reader:

                quantity = int(drug["Quantity"])
                price = float(drug["Price"])

                total = total + (quantity * price)

        print(
            "\nTotal Stock Value: ₹",
            total
        )


# ============================================
# MAIN PROGRAM
# ============================================

pharma = PharmaSystem()


while True:

    print("\n")
    print("===== PHARMA DRUG MANAGEMENT SYSTEM =====")

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

        print("Invalid choice!")