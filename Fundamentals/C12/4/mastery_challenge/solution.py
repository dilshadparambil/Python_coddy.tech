numbers = input()
prefix = input()
# Write your code below
new_num=numbers.split()
prefix_num=[]

for item in new_num:
    item=prefix+item
    prefix_num.append(item)

pr=' '.join(prefix_num)
print(pr)


