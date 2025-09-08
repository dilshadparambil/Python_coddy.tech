numbers = input().split()
# Write your code below
new_list=[]
new_list=([numbers[0]]+numbers+numbers[::-1]+[numbers[-1]])*2
print(new_list)