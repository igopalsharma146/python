def how_many(my_dict):
    return sum(len(value) for value in my_dict.values())

# Example usage:
animals = {'L': ['Lion'], 'D': ['Donkey'], 'E': ['Elephant']}
print("Sum of values count:", how_many(animals))
