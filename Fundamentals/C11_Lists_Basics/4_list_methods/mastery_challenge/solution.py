def combine_and_filter(lst, threshold):
    # Write code here
    new_list=[]
    for item in lst:
        if item>threshold:
            new_list.append(item)
    new_list.sort()
    return new_list