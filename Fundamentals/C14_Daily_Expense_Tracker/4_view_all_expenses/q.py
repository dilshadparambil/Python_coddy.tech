print("Welcome to the Daily Expense Tracker!")
print("\nMenu:\n1. Add a new expense\n2. View all expenses\n3. Calculate total and average expense\n4. Clear all expenses\n5. Exit")
expense_list=[]
game_on=True
while game_on:
    choice=int(input())
    if choice==1:
        exp_inp=float(input())
        expense_list.append(exp_inp)
        print("Expense added successfully!")
    elif choice==5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        game_on=False
