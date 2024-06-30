def how_many(my_dict):
    count=0
    for values in my_dict.values():
        # print(values)
        for value in values:
            # print(value)
            count+=1
    return count
animals = {'L': {'Lion',"5"}, 'D': {'Donkey',"4"}, 'E':{'Elephant'}}
print("Sum of values count:", how_many(animals))
