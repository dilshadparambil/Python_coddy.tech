# Write code here

try:
    num = int(input())  # This raises a ValueError
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print(f"You entered: {num}")
