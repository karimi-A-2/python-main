def my_for(iterable, func):
    iterator = iter(iterable)
    
    while True:
        try:
            # print(next(iterator))
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)


my_numbers = [1, 2, 3, 4]


def square(num):
    print(num ** 2)


my_for(my_numbers, print)
print('-------------')
my_for(my_numbers, square)
