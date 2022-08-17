L, R = map(int, input().split())
n = int(input())
index_count = dict()
for i in range(n):
    l, r = map(int, input().split())
    if R < l or r < L:
        continue
    # todo: make this part better to not check for key every time
    if l * 2 in index_count:
        index_count[l * 2] += 1
    else:
        index_count[l * 2] = 1
    if r * 2 + 1 in index_count:
        index_count[r * 2 + 1] -= 1
    else:
        index_count[r * 2 + 1] = -1
    
keys = list(index_count.keys())
keys.sort()

count = 0
i = 0
while i < len(keys) and keys[i] <= (2 * L):
    count += index_count[keys[i]]
    i += 1
min_value = count
max_value = count

while i < len(keys) and keys[i] <= (2 * R):
    count += index_count[keys[i]]
    if max_value < count:
        max_value = count
    if count < min_value:
        min_value = count
    i += 1

print(min_value, max_value)
