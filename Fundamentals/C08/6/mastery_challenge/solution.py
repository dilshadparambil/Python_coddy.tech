# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for i in range(32,81,4):
    print(i, end=", ")
print()  # new line


# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
count=0
for i in range(15,100,2):
    if count==8:
        break
    else:
        print(i, end=", ")
    count+=1
print()  # new line


# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for i in range(50,9,-5):
    print(i, end=", ")
print()  # new line


# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
prod=1
for i in range(3,31,3):
    prod*=i
print(prod)
