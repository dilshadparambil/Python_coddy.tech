lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
lst3=[]
for element in lst1:
    if element not in lst2:
        lst3.append(element)

print(lst3)