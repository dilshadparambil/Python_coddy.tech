lst = list(map(int, input().split(",")))
# Write your code below
index_lst=[]
for index,num in enumerate(lst):
    if num<50 or num%5==0:
        index_lst.append(index)
print(index_lst)