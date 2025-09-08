num=[]
num_count=int(input())
for i in range(num_count):
    temp=int(input())
    num.append(temp)

num_sum=0

for number in num:
    num_sum+=number

print(num_sum)