# 82  % --
from typing import Tuple

n, m = map(int, input().split())
edge_set = set()
for i in range(m):
    x, y = map(int, input().split())
    my_tuple: Tuple[int, int] = (x, y)
    if y < x:
        my_tuple = (y, x)
    edge_set.add(my_tuple)

q = int(input())

ans_list = []
for i in range(q):
    x, y = map(int, input().split())
    my_tuple: Tuple[int, int] = (x, y)
    if y < x:
        my_tuple = (y, x)
    if my_tuple in edge_set:
        ans_list.append('NO')
    else:
        ans_list.append('YES')

for ans in ans_list:
    print(ans)
    