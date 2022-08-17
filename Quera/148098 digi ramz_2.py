import math
import sys

n, first_cost = list(map(int, input().split()))

invests = list()

class Invest:
    def __init__(self, prof, cost, visited):
        self.prof = prof
        self.cost = cost
        self.visited = visited


for i in range(n):
    prof, cost = list(map(int, input().split()))
    invest = Invest(prof, cost, False)
    invests.append(invest)
sorat = float(first_cost)
makhraj = 0
min_val = sys.float_info.max
sort_count = 0
while True:
    if sort_count <= 1:
        def my_func(invest_compare):
            return (sorat + invest_compare.cost) / (makhraj + invest_compare.prof)
        invests.sort(key=my_func)
        sort_count += 1
    if len(invests) == 0:
        break
    removed = invests.pop(0)
    new_val = (sorat + removed.cost) / (makhraj + removed.prof)
    if new_val < min_val:
        removed.visited = True
        sorat += removed.cost
        makhraj += removed.prof
        min_val = new_val
    else:
        break

ceil = int(math.ceil(min_val))
print(ceil)
