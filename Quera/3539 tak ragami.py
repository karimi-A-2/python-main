a = int(input())
b = a
while b >= 10:
    sum_dig = 0
    while b != 0:
        sum_dig += b % 10
        b //= 10
    # print(sum_dig)
    b = sum_dig
print(b)
