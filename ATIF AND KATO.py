# Expense Tracker using Dictionary and Tuple

expenses = {}

while True:
    print("\n1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. Show All Expenses")
    print("5. Monthly Total")
    print("6. Weekly Total")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expenses[date] = (category, amount)
        print("Expense Added")

    # Update Expense
    elif choice == "2":
        date = input("Enter date to update: ")

        if date in expenses:
            category = input("Enter new category: ")
            amount = float(input("Enter new amount: "))
            expenses[date] = (category, amount)
            print("Expense Updated")
        else:
            print("No record found")

    # Delete Expense
    elif choice == "3":
        date = input("Enter date to delete: ")

        if date in expenses:
            del expenses[date]
            print("Expense Deleted")
        else:
            print("No record found")

    # Show All Expenses
    elif choice == "4":
        if expenses == {}:
            print("No expenses")
        else:
            for date in expenses:
                data = expenses[date]
                print(date, "->", data[0], "₹", data[1])

    # Monthly Total
    elif choice == "5":
        month = input("Enter month (YYYY-MM): ")
        total = 0

        for date in expenses:
            if date[:7] == month:
                total = total + expenses[date][1]

        print("Monthly Total =", total)

    # Weekly Total (simple method)
    elif choice == "6":
        week = input("Enter starting date of week (YYYY-MM-DD first 8 chars like 2026-02-1): ")
        total = 0

        for date in expenses:
            if date[:8] == week:
                total = total + expenses[date][1]

        print("Weekly Total =", total)

    # Exit
    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid choice")
