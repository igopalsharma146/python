# Using Concatenation:
# Python
original_tuple = (1, 2, 3)
new_element = 4
new_tuple = original_tuple + (new_element,)
print(new_tuple)  # Output: (1, 2, 3, 4)


# Using Tuple Unpacking:
original_tuple = (1, 2, 3)
new_element = 4
new_tuple = (*original_tuple, new_element)
print(new_tuple)  # Output: (1, 2, 3, 4)

# Converting to a List and Back to a Tuple:
original_tuple = (1, 2, 3)
new_element = 4
temp_list = list(original_tuple)
temp_list.append(new_element)
new_tuple = tuple(temp_list)
print(new_tuple)  # Output: (1, 2, 3, 4)