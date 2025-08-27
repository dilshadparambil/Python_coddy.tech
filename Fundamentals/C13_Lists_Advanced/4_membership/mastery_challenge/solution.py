def not_mutual_friends(list1, list2):
    # Write your code below
    list3=[]
    for friend in list1:
        if friend not in list2:
            list3.append(friend)
    for friend in list2:
        if friend not in list1:
            list3.append(friend)
    return list3