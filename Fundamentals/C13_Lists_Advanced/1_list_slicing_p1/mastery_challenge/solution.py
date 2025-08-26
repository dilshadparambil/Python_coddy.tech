input_list = input().split(', ')
# Write your code below
output_lst=[]
if len(input_list)>=5:
    output_lst.extend(input_list[:2])
    output_lst.extend(input_list[-2:])
else:
    output_lst.extend(input_list[:1])
    output_lst.extend(input_list[-1:])

print(output_lst)