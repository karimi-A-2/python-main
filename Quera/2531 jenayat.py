# : Memory Limit Exceeded
L, R = map(int, input().split())
n = int(input())
l_list = []
r_list = []
for i in range(n):
    l, r = map(int, input().split())
    if l > R or r < L:
        continue
    if l < L:
        l_list.append((L - L) * 2)
    else:
        l_list.append((l - L) * 2)
    if r > R:
        r_list.append((R - L) * 2)
    else:
        r_list.append((r - L) * 2)

length = (R - L) * 2 + 2
main_list = [0 for i in range(length)]
for index in l_list:
    main_list[index] += 1
for index in r_list:
    main_list[index + 1] -= 1
for i in range(length - 1):
    main_list[i + 1] += main_list[i]

main_list.pop()
min_value = min(main_list)
max_value = max(main_list)

print(min_value, max_value)
