tuple_numbers = (1, 2, 3, 4)
print(tuple_numbers)
# tuple_numbers are immutable you cannot change or assign

# tuple_numbers[0] = 2   # wrong:
# TypeError: 'tuple' object does not support item assignment

# tuple_numbers = (2, 3)
# we can create new tuple and assign it to previous tuple reference holder

# new_tuple = tuple(1, 2, 3, 4)  # wrong:
# TypeError: tuple expected at most 1 argument, got 4
# we should pass list of numbers to tuple()

new_tuple = tuple([5, 6, 7, 8])  # correct
print(new_tuple)
