def elements_of_freedom(elements):
    # Your solution here
    
    # Step 1: Filter elements with length >= 5
    filter1=[element for element in elements if len(element)>=5]
    # Step 2: Convert filtered elements to uppercase
    filter2=[element.upper() for element in filter1]
    # Step 3: Create a list of unique elements
    filter3=[]
    for item in filter2:
        if item not in filter3:
            filter3.append(item)
    # Step 4: Return the final result
    return filter3