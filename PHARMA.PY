# PHARMA DRUG MANAGEMENT SYSTEM
# Beginner Python Project
# Features:
# 1. Add Drug
# 2. Display Drugs
# 3. Search Drug
# 4. Update Stock
# 5. Remove Drug
# 6. Check Low Stock
# 7. Check Expired Drugs
# 8. Exit

import csv
from datetime import datetime

FILE = "pharma_drugs.csv"


# Create CSV file if it does not exist
def create_file():
    try:
        open(FILE, "r").close()
    except FileNotFoundError:
        with open(FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Drug_ID", "Brand_Name", "Generic_Name",
                "Category", "Quantity", "Price",
                "Expiry_Date", "Manufacturer", "Batch_Number"
            ])


# Add a new drug
def add_drug():
    drug_id = input("Enter Drug ID: ")
    brand = input("Enter Brand Name: ")
    generic = input("Enter Generic Name: ")
    category = input("Enter Category: ")
    quantity = input("Enter Quantity: ")
    price = input("Enter Price: ")
    expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
    manufacturer = input("Enter Manufacturer: ")
    batch = input("Enter Batch Number: ")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            drug_id, brand, generic, category,
            quantity, price, expiry, manufacturer, batch
        ])

    print("Drug added successfully!")


# Display all drugs
def display_drugs():
    with open(FILE, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print("No drugs available.")
        return

    for row in data:
        print(row)


# Search drug
def search_drug():
    search = input("Enter Drug ID or Brand Name: ").lower()
    found = False

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (row["Drug_ID"].lower() == search or
                    row["Brand_Name"].lower() == search):
                print("\nDrug Found")
                for key, value in row.items():
                    print(key, ":", value)
                found = True

    if not found:
        print("Drug not found.")


# Update stock
def update_stock():
    drug_id = input("Enter Drug ID: ")
    new_quantity = input("Enter New Quantity: ")

    rows = []

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["Drug_ID"] == drug_id:
                row["Quantity"] = new_quantity
                print("Stock updated successfully!")
            rows.append(row)

    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# Remove drug
def remove_drug():
    drug_id = input("Enter Drug ID to remove: ")

    rows = []
    found = False

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["Drug_ID"] == drug_id:
                found = True
            else:
                rows.append(row)

    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    if found:
        print("Drug removed successfully!")
    else:
        print("Drug not found.")


# Check low stock
def low_stock():
    print("\nLow Stock Drugs:")

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row["Quantity"]) < 20:
                print(
                    row["Drug_ID"],
                    row["Brand_Name"],
                    "Quantity:", row["Quantity"]
                )


# Check expired drugs
def expired_drugs():
    today = datetime.today().date()
    found = False

    print("\nExpired Drugs:")

    with open(FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expiry = datetime.strptime(
                row["Expiry_Date"], "%Y-%m-%d"
            ).date()

            if expiry < today:
                print(
                    row["Drug_ID"],
                    row["Brand_Name"],
                    "Expiry:", row["Expiry_Date"]
                )
                found = True

    if not found:
        print("No expired drugs.")


# Main program
create_file()

while True:
    print("\n===== PHARMA DRUG MANAGEMENT SYSTEM =====")
    print("1. Add Drug")
    print("2. Display Drugs")
    print("3. Search Drug")
    print("4. Update Stock")
    print("5. Remove Drug")
    print("6. Check Low Stock")
    print("7. Check Expired Drugs")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_drug()

    elif choice == "2":
        display_drugs()

    elif choice == "3":
        search_drug()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        remove_drug()

    elif choice == "6":
        low_stock()

    elif choice == "7":
        expired_drugs()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")