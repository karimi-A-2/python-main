my_dictionary = {
    'name': 'item 1',
    'count': 3,
    'price': 2500,
    3: True,
    '3': False,
}

# print keys
for key in my_dictionary:
    print(key)
print('-------------')

# prin values
for key in my_dictionary:
    print(my_dictionary[key])
print('-------------')

# print keys
print(my_dictionary.keys())
for key in my_dictionary.keys():
    print(key)

# prin values
print(my_dictionary.values())
for value in my_dictionary.values():
    print(value)

print(my_dictionary.items())
for item in my_dictionary.items():
    print(item)
for key, value in my_dictionary.items():
    print(key, value)
