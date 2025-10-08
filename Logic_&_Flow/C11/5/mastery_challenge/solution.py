def print_sequence(n):
    # Write code here
    if n==0:
        print("Blast off!")
        return 0
    print(f"T-minus {n}")
    return print_sequence(n-1)
