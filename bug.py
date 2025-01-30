def function_with_uncommon_error(data):
    # This function demonstrates a subtle bug involving mutable default arguments.
    result = []
    for item in data:
        result.append(item.upper())
    return result

# The bug is revealed when calling the function multiple times:
my_list = ['a', 'b', 'c']
print(function_with_uncommon_error(my_list)) # Output: ['A', 'B', 'C']
print(function_with_uncommon_error([]))     # Output: []
my_list = ['x','y','z']
print(function_with_uncommon_error(my_list)) # Output: ['X', 'Y', 'Z']

# The unexpected behavior is that the list is altered even after a call with an empty list.