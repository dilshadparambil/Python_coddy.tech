def count_down(n):
    # Write code here
    print(n)
    if n==0:
        return 0
    return count_down(n-1)
