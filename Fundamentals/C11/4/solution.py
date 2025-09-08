def merge(lst1, lst2):
    # Write code here
    for element in lst2:
        lst1.append(element)
        
    lst1.sort()
    return lst1