num1=int(input())
num2=int(input())

for i in range(num1,num2):
    if i%2==0 and i>5:
        print(f"First even number greater than 5: {i}")
        break

for j in range(num1,num2):   
    if j%7==0:
        print(f"First number divisible by 7: {j}")
