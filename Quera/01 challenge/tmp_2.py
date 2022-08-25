split = list(map(int, input().split()))
sum_nums_2 = 0
sum_nums_3 = 0
for item in split:
    sum_nums_2 += item ** 2
    sum_nums_3 += item ** 3
print(sum_nums_2, sum_nums_3)

n = 8
sum_glob_1 = n * (n + 1) // 2
sum_glob_2 = n * (n + 1) * (2 * n + 1) // 6
sum_glob_3 = (n ** 2) * ((n + 1) ** 2) // 4
print(sum_glob_2, sum_glob_3)
# 1 1 3 6 6 6 6 7
