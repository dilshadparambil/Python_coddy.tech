def frequency_counter(data_list):
    # Write code here
    dict={}
    
    for item in data_list:
        count=0
        key=item
        for item in data_list:
            if key==item:
                count+=1
        dict[key]=count
    
    return dict

