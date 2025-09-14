def filter_and_square_set(input_set):
    # Write code here
    new_set=set()
    for i in input_set:
        if i%2!=0:
            sqnum=i*i
            new_set.add(sqnum)
        
    return new_set