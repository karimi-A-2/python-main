# all()
# Return True if bool(x) is True for all values x in the iterable.
# If the iterable is empty, return True.

numbers = [0, 2, 3, 4]
print([bool(x) for x in numbers])
print(all(numbers))
print(all([]))


numbers = [2, 4, 6, 7]
print([num % 2 == 0 for num in numbers])
print(all([num % 2 == 0 for num in numbers]))
