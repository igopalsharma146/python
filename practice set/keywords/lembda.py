'''
A lambda function in Python is a small, anonymous function defined using the lambda keyword. Unlike regular
functions created with the def keyword, lambda functions are typically used for short, simple operations.
'''


'''
#lambda arguments: expression

arguments: The parameters the function takes.
expression: A single expression that is evaluated and returned.
'''

add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15


'''
Use Cases
Lambda functions are often used in situations where a small, throwaway function is needed, such as:

Sorting: Using a lambda function as a key for sorting.
Filtering: Using a lambda function with filter().
Mapping: Using a lambda function with map().
'''

numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
