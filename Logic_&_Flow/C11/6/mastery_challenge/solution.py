def sum_digits(n):
    # Write code here
    if n<10:
        return n
    else:
        lastdigit=n%10
        balance=n//10
        return sum_digits(balance)+lastdigit