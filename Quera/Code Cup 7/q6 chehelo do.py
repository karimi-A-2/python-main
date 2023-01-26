n = int(input())
arr = list(map(int, input().split()))

new_arr = []
for item in arr:
    if item < 42:
        continue
    else:
        new_arr.append(item - 42)

print(new_arr)
