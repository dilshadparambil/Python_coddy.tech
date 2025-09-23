def dictionary_sorter(data_dict):
    # Write code here
   return {key: data_dict[key] for key in sorted(data_dict , key=data_dict.get)}