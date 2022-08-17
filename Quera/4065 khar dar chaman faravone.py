a, b, l = map(int, input().split())

n = 0
sum_val = 0
while True:
    sum_val += a
    n += 1
    if n == l:
        break
    sum_val += b
    n += 1
    if n == l:
        break
print(sum_val)