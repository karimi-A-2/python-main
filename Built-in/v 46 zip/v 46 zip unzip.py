numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8, 9, 10]

zip_obj = zip(numbers_1, numbers_2)

unzipped = zip(*zip_obj)
print(unzipped)  # <zip object at 0x102aa9c80>
x, y = unzipped
print(list(x))
print(list(y))

myList = [(1, 5), (3, 7), (6, 4), (7, 9)]
unzipped = zip(*myList)
print(list(unzipped))

# print(list(unzipped))
