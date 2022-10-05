n, m = map(int, input().split(maxsplit=1))

p_set = set()
for _ in range(m):
    a, b = map(int, input().split(maxsplit=1))
    p_set.add((a, b))

min_ = m

for i in range(1, m + 1):
    if m % i == 0:
        x = i
        y = m // i
        if x > n:
            break
        if y > n:
            continue
        
        # print(x, y)
        
        for xx in range(n - x + 1):
            for yy in range(n - y + 1):
                count = 0
                for ii in range(1, x + 1):
                    for jj in range(1, y + 1):
                        if (ii + xx, jj + yy) not in p_set:
                            count += 1
                if count < min_:
                    min_ = count

print(min_)
