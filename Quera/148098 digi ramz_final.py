import math
import sys

n, first_cost = list(map(int, input().split()))

invests = list()


class Invest:
    def __init__(self, prof, cost):
        self.prof = prof
        self.cost = cost


for i in range(n):
    prof, cost = list(map(int, input().split()))
    invest = Invest(prof, cost)
    invests.append(invest)
sorat = float(first_cost)
makhraj = 0
min_val = sys.float_info.max


def my_func(invest_compare):
    return (sorat + invest_compare.cost) / (makhraj + invest_compare.prof)


invests.sort(key=my_func)

while len(invests) != 0:
    removed = invests.pop(0)
    new_val = (sorat + removed.cost) / (makhraj + removed.prof)
    if new_val >= min_val:
        break
    sorat += removed.cost
    makhraj += removed.prof
    min_val = new_val

ceil = int(math.ceil(min_val))
print(ceil)
