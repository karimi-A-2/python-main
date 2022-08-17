n = int(input())
string = input().strip()
arr = []  # Dynamic Programming
for i in range(len(string)):
    if string[i] == 'B':
        arr.append(1)
    elif string[i] == 'T':
        arr.append(0)
    elif string[i] == '.' or string[i] == 'K':
        sum_last_three = 0
        sum_last_three += arr[i - 1]
        if not ((i - 2) < 0):
            sum_last_three += arr[i - 2]
        if not ((i - 3) < 0):
            sum_last_three += arr[i - 3]
        arr.append(sum_last_three)
print(arr[-1])
