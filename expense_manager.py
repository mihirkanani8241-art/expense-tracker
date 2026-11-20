from datetime import datetime

from storage import load_expenses, save_expenses


def add_expense(date, description, category, amount):
    datetime.strptime(date, "%Y-%m-%d")

    if not description.strip():
        raise ValueError("Description cannot be empty")

    if not category.strip():
        raise ValueError("Category cannot be empty")

    amount = float(amount)

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    expenses = load_expenses()

    existing_ids = [int(expense["id"]) for expense in expenses]
    new_id = max(existing_ids, default=0) + 1

    new_expense = {
        "id": str(new_id),
        "date": date,
        "description": description,
        "category": category,
        "amount": str(amount)
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense


def list_expenses():
    return load_expenses()


def delete_expense(expense_id):
    expenses = load_expenses()

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != str(expense_id)
    ]

    if len(expenses) == len(updated_expenses):
        return False

    save_expenses(updated_expenses)
    return True


def get_summary():
    expenses = load_expenses()

    total = sum(
        float(expense["amount"])
        for expense in expenses
    )

    return total


def get_monthly_summary(month):
    datetime.strptime(month, "%Y-%m")

    expenses = load_expenses()

    monthly_expenses = [
        expense for expense in expenses
        if expense["date"].startswith(month)
    ]

    total = sum(
        float(expense["amount"])
        for expense in monthly_expenses
    )

    return total


def get_category_summary():
    expenses = load_expenses()
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary