# 78  % --
from typing import Tuple

n, m = map(int, input().split())
matrix = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    if x < y:
        matrix[x - 1][y - 1] = 1
    else:
        matrix[y - 1][x - 1] = 1

q = int(input())

ans_list = []
for i in range(q):
    x, y = map(int, input().split())
    my_tuple: Tuple[int, int] = (x, y)
    if x < y:
        is_exists = matrix[x - 1][y - 1] == 1
    else:
        is_exists = matrix[y - 1][x - 1] == 1
    if is_exists:
        ans_list.append('NO')
    else:
        ans_list.append('YES')

for ans in ans_list:
    print(ans)
    