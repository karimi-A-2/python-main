# map_obj = map(func, *iterable)

numbers = [1, 2, 3, 4, 5]

# method 1: map(func, *iterable)
doubles_map_obj = map(lambda x: x * 2, numbers)
print(doubles_map_obj)              # <map object at 0x1031f3940>
print(list(doubles_map_obj))        # [2, 4, 6, 8, 10]
print(list(doubles_map_obj))        # []  ? --> if we iterate throw map obj it will empty

out_1, out_2, out_3, out_4, out_5 = map(lambda x: x * 2, numbers)  # todo: why is it working?
print(out_1, out_2, out_3, out_4, out_5)

doubles_map_obj = map(lambda x: x * 2, numbers)
# print(doubles_map_obj[2])     # wrong: TypeError: 'map' object is not subscriptable
for item in doubles_map_obj:    # correct iterable
    print(item)

# method 2: for
doubles = []
for num in numbers:
    doubles.append(num * 2)
print(doubles)

names = ["mohammad", "sara", "iman", "ali"]
upperNames = map(lambda name: name.upper(), names)
print(list(upperNames))

people = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'sara', 'family': 'moradi', 'age': 25},
    {'name': 'iman', 'family': 'madaeny', 'age': 30}
]
print(list(map(lambda person: person['family'], people)))

families_2 = []
for person in people:
    families_2.append(person['family'])
print(families_2)
