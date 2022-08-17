def fib_generator(max):
    x = 0
    y = 1
    count = 0

    while count < max:
        x, y = y, x + y
        yield y
        count += 1


for num in fib_generator(30000):
    print(num)
