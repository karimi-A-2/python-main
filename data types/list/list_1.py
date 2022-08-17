i_list = [0, 3, 2]
print(i_list[:3])
i_max = max(i_list)
while max(i_list) == i_max:
    i_list.remove(max(i_list))
runner_up = max(i_list)
print(runner_up)
