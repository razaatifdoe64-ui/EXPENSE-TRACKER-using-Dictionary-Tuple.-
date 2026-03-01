expenses = {}

while True:
    print("Menu")
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. Show Expenses")
    print("5. Monthly Total")
    print("6. Weekly Total")
    print("7. Exit")

    option = input("Enter option: ")

    if option == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expenses[date] = (category, amount)
        print("Expense added")

    elif option == "2":
        date = input("Enter date to update: ")

        if date in expenses:
            category = input("Enter new category: ")
            amount = float(input("Enter new amount: "))
            expenses[date] = (category, amount)
            print("Expense updated")
        else:
            print("Record not found")

    elif option == "3":
        date = input("Enter date to delete: ")

        if date in expenses:
            del expenses[date]
            print("Expense deleted")
        else:
            print("No data for this date")

    elif option == "4":
        if expenses == {}:
            print("No expense is there")
        else:
            for d in expenses:
                print(d, expenses[d])

    elif option == "5":
        month = input("Enter month (YYYY-MM): ")
        total = 0
        for d in expenses:
            if month in d:
                total = total + expenses[d][1]
        print("Total of this month is", total)

    elif option == "6":
        start = input("Enter week start date (YYYY-MM-DD): ")
        total = 0
        for d in expenses:
            if d >= start:
                total = total + expenses[d][1]
        print("Week total is", total)

    elif option == "7":
        print("Program closed")
        break

    else:
        print("Wrong option choose again")
