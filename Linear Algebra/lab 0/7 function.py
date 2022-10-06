def add(a, b):
    return a + b


print(add(2, 3))
print(add(2, 3.1))
print(add('abc', '123'))


def sum_(l):
    s = 0
    for k in l:
        s += k
    return s


l = [1, 2, 4, 8, 16]
print(sum_(l))
print(sum_(range(10)))
print(sum_(2))  # error


def add(a, b=1):
    return a + b


print(add(20, 4))
print(add(20))


def sub(n1, n2):
    return n1 - n2


print(sub(20, 4))
print(sub(n1=20, n2=4))
print(sub(n2=20, n1=4))
