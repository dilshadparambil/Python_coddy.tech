def house_of_lists(list_of_lists):
    # Write code here
   
    filter1=[lst for lst in list_of_lists if sum(lst)<=50]
    filter2 = [num for lst in filter1 for num in lst if num < 5]
    return filter2
