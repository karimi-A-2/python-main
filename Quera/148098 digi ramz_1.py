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
count = 0
while True:
    remove = -1
    for i in range(len(invests)):
        invest = invests[i]
        if invest.visited:
            continue
        new_val = (sorat + invest.cost) / (makhraj + invest.prof)
        if new_val < min_val:
            min_val = new_val
            remove = i
    if count >= 90:
        break
    if remove == -1:
        break
    to_be_removed = invests[remove]
    to_be_removed.visited = True
    sorat += to_be_removed.cost
    makhraj += to_be_removed.prof
    count += 1
    
ceil = int(math.ceil(min_val))
print(ceil)
