t = int(input())
final_ans = []

for i in range(t):
    n = int(input())
    out = 0
    if n % 3 != 0:
        out = (n // 3) + 1
    else:
        if n <= 12:
            out = n // 3
        else:
            out = (n // 3) + 1
    final_ans.append(out)

for item in final_ans:
    print(item)
