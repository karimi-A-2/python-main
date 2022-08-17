string = input()

ans = 1
for char in string:
    if char == 'D' or char == 'T' or char == 'F' or char == 'L':
        ans *= 2
    else:
        continue
print(ans)
