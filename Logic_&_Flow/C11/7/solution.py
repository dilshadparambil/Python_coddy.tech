def sum_nested(nested_list):
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):
            total_sum += sum_nested(element)  # Recursively call for sublists
        else:
            total_sum += element  # Add integer elements
    return total_sum
