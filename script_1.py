def get_unique_list(my_list):
    temp_list = set(my_list)
    unique = (list(temp_list))
    for each in unique:
        print (each)



my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)

