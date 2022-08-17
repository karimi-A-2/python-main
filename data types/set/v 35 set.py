numbers = {1, 2, 3, 4, 4, 4, 4, 4, 2, 2, 5}
# numbers_3 = {}  # wrong --> it creates dictionary not set
print(numbers)  # duplicate numbers will count as one {1, 1, 1} == {1} it is like set in reality

for item in numbers:
    print(item)

# print(numbers[0])  # wrong:
# TypeError: 'set' object is not subscriptable
# Class 'set' does not define '__getitem__', so the '[]' operator cannot be used on its instances.

print(4 in numbers)

numbers_2 = {3, 5, 't', 'z', 2, 7, 1, 1, 1, 5, 5, 5, 5}
print(numbers_2)

for item in numbers_2:
    print(item)

courses_list = ["kotlin", "vuejs", "python", "ionic"]
courses_set = set(courses_list)
print(courses_set)

print(list(numbers_2))

numbers = {1, 2, 3, 4}
numbers.add(4)  # if item exists do nothing

if 4 in numbers:
    numbers.remove(4)  # remove item. raise KeyError if item is not preset
numbers.discard(4)     # remove item. won't raise KeyError if item is not preset

copyNumbers = numbers.copy()
print(numbers is copyNumbers)

numbers.clear()
print(numbers)

python = {"ali", "milad", "mohammad", "sara"}
kotlin = {"mohammad", "ahmad", "reza", "ali"}

print(python | kotlin)  # union
print(python & kotlin)  # intersection

newSet = {x ** 2 for x in range(10)}  # set comprehension
print(newSet)

characters = {char for char in "hello world"}
print(characters)
