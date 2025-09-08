lst = input().split()
# Write your code below
index_lst=[]
for index,word in enumerate(lst):
    if len(word)>3 or word.startswith('a'):
        index_lst.append(index)
print(index_lst)