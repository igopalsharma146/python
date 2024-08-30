numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))  # Output: [2, 4, 6, 8]


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]


strings = ['sat', 'bat', 'cat', 'mat']
result = map(list, strings)
print(list(result))  # Output: [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
