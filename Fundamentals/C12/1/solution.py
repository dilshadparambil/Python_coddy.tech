lst = input().split(",")
# Write your code below
new_lst=[]
for word in lst:
    if len(word)>5:
        new_lst.append(word)

print(new_lst)
