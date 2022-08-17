n = int(input())
max_count = 0
for i in range(n):
    s = input()
    my_set = set()
    for char in s:
        my_set.add(char)
    length = len(my_set)
    if length >= max_count:
        max_count = length

print(max_count)
