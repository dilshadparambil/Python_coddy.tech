print("Welcome to the Daily Expense Tracker!")
print("\nMenu:\n1. Add a new expense\n2. View all expenses\n3. Calculate total and average expense\n4. Clear all expenses\n5. Exit")
    
game_on=True
while game_on:
    choice=int(input())
    if choice==5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        game_on=False
