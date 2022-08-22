numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]

zip_obj = zip(numbers_1, numbers_2)
print(zip_obj)  # <zip object at 0x1015a1a00> --> print address of zip object
print(list(zip_obj))  # [(1, 5), (2, 6), (3, 7), (4, 8)] // list of tuple
next(zip_obj)  # StopIteration
print(list(zip_obj))  # [] // empty because shortest iterator is exhausted(consumed)

