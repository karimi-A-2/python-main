A, B, m = map(int, input().split(maxsplit=2))
n = int(input())


def get_dice(n):
    x = B
    dice = (x % 6) + 1
    yield dice
    for _ in range(n - 1):
        x = ((A * x) + B) % m
        dice = (x % 6) + 1
        yield dice


for d in get_dice(n):
    print(d)
