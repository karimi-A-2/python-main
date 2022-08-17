start_list = list(map(int, input().split()))
finish_list = list(map(int, input().split()))
print(start_list)
print(finish_list)

if len(start_list) != len(finish_list):
    raise ValueError('len(start_list) != len(finish_list)')

ans_list = []
max_count = 0
current_end = 0
my_dict = dict()


def my_lambda(item):
    return item[1]


list(my_dict.items()).sort(key=my_lambda)

for i in range(len(start_list)):
    if start_list[i] >= current_end:
        max_count += 1
        current_end = finish_list[i]
        ans_list.append(i)
    else:
        continue
print(ans_list)
print(f'max number of activities: {max_count}')
