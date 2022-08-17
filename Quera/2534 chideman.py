n = int(input())
num_list = []
sum_val = 0
for i in range(n):
    value = int(input())
    sum_val += value
    num_list.append(value)

average = sum_val // n
sum_difference = 0
for i in num_list:
    difference = average - i
    sum_difference += abs(difference)
print(sum_difference // 2)
