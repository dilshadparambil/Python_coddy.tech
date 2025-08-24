numbers = input().split(',')
# Write your code below
sum_even=0
for num in numbers:
    if int(num)%2==0:
        sum_even+=int(num)

print(sum_even)