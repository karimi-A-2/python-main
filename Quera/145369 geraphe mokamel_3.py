# 100 % :)
n, m = map(int, input().split())
my_list = [set() for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    my_list[x - 1].add(y - 1)
    my_list[y - 1].add(x - 1)

q = int(input())

ans_list = []
for i in range(q):
    x, y = map(int, input().split())
    if y - 1 in my_list[x - 1]:
        ans_list.append('NO')
    else:
        ans_list.append('YES')

for ans in ans_list:
    print(ans)
