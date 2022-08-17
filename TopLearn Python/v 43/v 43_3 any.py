# any()
# Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty, return False.

numbers = [2, 4, 6, 8]
print(any([num % 2 != 0 for num in numbers]))

results = [False, False, False, True]
print(any(results))

