input_str = input()
i = 0
s = 0
out_list = []

for char in input_str:
    if char == '=':
        if len(out_list) != 0:
            out_list.pop()
    else:
        out_list.append(char)
print(''.join(out_list))
