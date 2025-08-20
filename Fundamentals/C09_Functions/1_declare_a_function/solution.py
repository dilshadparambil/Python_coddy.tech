def sum_num():
    sum_of=0
    for i in range(1,10001):
        sum_of+=i
    print(sum_of)

num_count=int(input())

for i in range(num_count):
    sum_num()