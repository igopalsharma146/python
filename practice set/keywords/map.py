'''The map keyword in Python is used with the map() function, which applies a specified function to each item in an iterable (like a list or tuple) and returns a map object (an iterator). Here’s a detailed look:


map(function, iterable, ...)

function: The function to apply to each item.
iterable: One or more iterables whose items will be passed to the function.
'''
def double(n):
    return n * 2

numbers = [1, 2, 3, 4]
result = map(double, numbers)
print(list(result))  # Output: [2, 4, 6, 8]

