lst = input().split(",")
# Write your code below
if len(lst)%2!=0:
    item1=len(lst)//2-1
    item2=len(lst)//2+2
    print(lst[item1:item2])
else:
    item1=len(lst)//2-1
    item2=len(lst)//2+1
    print(lst[item1:item2])
