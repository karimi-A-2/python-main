# normal function
def square_1(num):
    return num * num


# one line function with def
def square_2(num): return num * num


# one line lambda # PEP 8: E731 do not assign a lambda expression, use a def
square_3 = lambda num: num * num

print(square_1(6))
print(square_2(6))
print(square_3(6))
print((lambda num: num * num)(6))


def sum(first, second): return first + second
print(sum(4, 7))


sum_2 = lambda first, second: first + second
print(sum_2(4, 8))


print(square_1.__name__)
print(square_2.__name__)
print(square_3.__name__)  # lambda: anonymous functions ==> no name
