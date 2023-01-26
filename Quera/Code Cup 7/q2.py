import math
n = int(input())

for _ in range(n):
    x1, y1, x2, y2 = map(float, input().split())
    if x1 == 0 and x2 == 0:
        out = abs(y1 - y2)
        print("%.12f" % out)
    elif y1 == 0 and y2 == 0:
        out = abs(x1 - x2)
        print("%.12f" % out)
    else:
        a = x1 + y1
        a = abs(a)
        b = x2 + y2
        b = abs(b)
        min_ = min(a, b)
        max_ = max(a, b)
        out = ((math.pi / 2) * min_) + (max_ - min_)
        print("%.12f" % out)
    