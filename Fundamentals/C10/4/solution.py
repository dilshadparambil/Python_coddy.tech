print("Welcome to FizzBuzz!")
def fizzbuzz(num):
    if num%3==0 and num%7==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%7==0:
        return "Buzz"
    elif '3' in str(num):
        return "Almost Fizz" 
    else:
        return num

num=int(input())
for i in range(1,num+1):
    answer=fizzbuzz(i)
    print(answer)