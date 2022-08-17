n, k = map(int, input().split())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)


def get_max_length(num_list):
    max_length = 0
    previous = num_list[0]
    length = 1
    i = 1
    while i < len(num_list):
        if num_list[i] != previous:
            previous = num_list[i]
            if max_length < length:
                max_length = length
            length = 1
        else:
            length += 1
        i += 1
    if max_length < length:
        max_length = length
    return max_length


print(get_max_length(num_list))
