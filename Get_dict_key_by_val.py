# Get key by value in dictionary
dictionary = {'george' : 16, 'amber' : 19}
search_age = 19
def get_dict_key_by_val(dict_in, val_in):
    for ky, val in dict_in.items():
        if val == val_in:
            return ky
        
print(get_dict_key_by_val(dictionary, search_age))