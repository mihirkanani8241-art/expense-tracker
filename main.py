import argparse

from expense_manager import (
    add_expense,
    list_expenses,
    delete_expense,
    get_summary,
    get_monthly_summary,
    get_category_summary
)


parser = argparse.ArgumentParser(
    description="Personal Expense Tracker"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)


# ADD COMMAND
add_parser = subparsers.add_parser("add")

add_parser.add_argument("--date", required=True)
add_parser.add_argument("--description", required=True)
add_parser.add_argument("--category", required=True)
add_parser.add_argument("--amount", type=float, required=True)


# LIST COMMAND
subparsers.add_parser("list")


# DELETE COMMAND
delete_parser = subparsers.add_parser("delete")

delete_parser.add_argument("id", type=int)


# SUMMARY COMMAND
summary_parser = subparsers.add_parser("summary")

summary_parser.add_argument("--month")


# CATEGORY SUMMARY COMMAND
subparsers.add_parser("categories")


# EXECUTE COMMAND
args = parser.parse_args()

try:

    if args.command == "add":

        expense = add_expense(
            args.date,
            args.description,
            args.category,
            args.amount
        )

        print(
            f"Expense added successfully. ID: {expense['id']}"
        )

    elif args.command == "list":

        expenses = list_expenses()

        if not expenses:
            print("No expenses found.")

        for expense in expenses:
            print(
                f"ID: {expense['id']} | "
                f"Date: {expense['date']} | "
                f"Description: {expense['description']} | "
                f"Category: {expense['category']} | "
                f"Amount: ₹{expense['amount']}"
            )

    elif args.command == "delete":

        result = delete_expense(args.id)

        if result:
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")

    elif args.command == "summary":

        if args.month:
            total = get_monthly_summary(args.month)
            print(f"Monthly expenses: ₹{total:.2f}")

        else:
            total = get_summary()
            print(f"Total expenses: ₹{total:.2f}")

    elif args.command == "categories":

        summary = get_category_summary()

        if not summary:
            print("No expenses found.")

        for category, amount in summary.items():
            print(f"{category}: ₹{amount:.2f}")

except ValueError as error:
    print(f"Error: {error}")