def manage_list(list1, element_to_append, index_to_remove):
    # Write code here
    list1.append(element_to_append)
    if index_to_remove<len(list1) in list1:
        list1.pop(index_to_remove)
    if len(list1)>3:
        return "The list has more than 3 elements"
    return "The list has 3 or fewer elements"

print(manage_list([1,2,3],4,5))