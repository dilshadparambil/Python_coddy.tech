print("Welcome to FizzBuzz!")
def fizzbuzz(num):
    if num%3==0 and num%7==0:
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%7==0:
        return "Buzz"
    else:    
        return num

num=int(input())
answer=fizzbuzz(num)
print(answer)