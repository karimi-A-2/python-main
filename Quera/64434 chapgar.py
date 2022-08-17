n, m = map(int, input().split())


def print_start(n):
    for i in range(n):
        print('X', end='')


def print_dot(n):
    for i in range(n):
        print('.', end='')


def print_ln():
    print('')


for i in range(n):
    print_start(m)
    print_dot(m)
    print_start(m)
    print_ln()
for i in range(n):
    print_dot(m)
    print_start(m)
    print_dot(m)
    print_ln()
for i in range(n):
    print_start(m)
    print_dot(m)
    print_start(m)
    print_ln()