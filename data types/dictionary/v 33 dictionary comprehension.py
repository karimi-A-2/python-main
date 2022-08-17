# list comprehension:
list_numbers = [1, 2, 3, 4, 5]
doubledNumbers = [num * 2 for num in list_numbers]
print(doubledNumbers)

# dictionary comprehension
dict_numbers = dict(first=1, second=2, third=3)
print(dict_numbers)

# wrong: ValueError: too many values to unpack (expected 2)
# squareNumber = {key: value for key, value in dict_numbers}
# correct: use dict_obj.items()
squareNumber = {key: value ** 2 for key, value in dict_numbers.items()}
print(squareNumber)

simpledNumbers = {num: num for num in [1, 2, 3, 4]}
print(simpledNumbers)
doubledNumbers = {num: num * 2 for num in [1, 2, 3, 4]}
print(doubledNumbers)
conditionNumbers = {num: ('even' if num % 2 == 0 else 'odd') for num in [1, 2, 3, 4]}
print(conditionNumbers)
