"""Expense Tracker - console-based personal finance tool."""

from datetime import date

expenses = []  # list of dictionaries


def add_expense():
    """Record a new expense (date, category, description, amount)."""
    day = input("Date (YYYY-MM-DD, Enter for today): ").strip() or str(date.today())
    category = input("Category (Food, Travel, Books...): ").strip() or "General"
    description = input("Description: ").strip()
    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount. Expense not added.\n")
        return
    if amount <= 0:
        print("Amount must be positive. Expense not added.\n")
        return

    expenses.append(
        {"date": day, "category": category, "description": description, "amount": amount}
    )
    print("Expense added!\n")


def view_expenses():
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print(f"\n{'No':<4}{'Date':<12}{'Category':<12}{'Description':<20}{'Amount':>10}")
    print("-" * 58)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4}{e['date']:<12}{e['category']:<12}{e['description']:<20}{e['amount']:>10.2f}")
    print()


def total_spending():
    """Show total spending and a per-category summary."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("\nSpending by category:")
    for category, amount in totals.items():
        print(f"  {category:<12}{amount:>10.2f}")
    print(f"\nTotal spending: {sum(totals.values()):.2f}\n")


def main():
    menu = {"1": add_expense, "2": view_expenses, "3": total_spending}
    while True:
        print("=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Calculate total spending")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "4":
            print("Goodbye! Track smart, spend smart.")
            break
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
