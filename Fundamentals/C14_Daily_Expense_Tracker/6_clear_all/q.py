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
    elif choice==2:
        if not expense_list:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for sno in range(1,len(expense_list)+1):
                print(f"{sno}. {expense_list[sno-1]}")
    elif choice==3:
        if not expense_list:
            print("No expenses recorded yet.")
        else:
            total=sum(expense_list)
            average=total/len(expense_list)
            print(f"Total expense: {total}\nAverage expense: {average}")

    elif choice==5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        game_on=False
