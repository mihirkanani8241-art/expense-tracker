import csv
from pathlib import Path

FILE_NAME = Path(__file__).with_name("expenses.csv")

FIELDNAMES = ["id", "date", "description", "category", "amount"]


def load_expenses():
    if not FILE_NAME.exists():
        return []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)