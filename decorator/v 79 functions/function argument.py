def sum(number, func):
    total = 0
    for num in range(1, number + 1):  # [1,2,3,4,5]
        total += func(num)
    return total


def square(x):
    return x * x


print(sum(5, square))

# 1 + 2 + 3 + 4 + 5 = 15

# 1 + 4 + 9 + 16 + 25 = 55
