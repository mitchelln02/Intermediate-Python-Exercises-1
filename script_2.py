def get_combined_dict(dict1,dict2):
    for x in dict2:
        if x in dict1:
            dict2[x] = dict2[x] + dict1[x]
    print(dict2)


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)


