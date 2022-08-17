n = int(input())
all_time = [0 for i in range(60 * 24)]
for i in range(n):
    name, time, sign = input().split()
    hour, minute = map(int, time.split(':'))
    point = (hour * 60) + minute
    if sign == '+':
        all_time[point] += 1
    elif sign == '-':
        all_time[point] -= 1

for i in range(60 * 24 - 1):
    all_time[i + 1] += all_time[i]
    
max_point = -1
max_num = -500000
for i in range(60 * 24):
    if all_time[i] > max_num:
        max_num = all_time[i]
        max_point = i
    
out_hour = max_point // 60
out_minute = max_point % 60


def get_out_str(hour, minute):
    out_str = ''
    if hour < 10:
        out_str += '0'
    out_str += f'{hour}'
    out_str += ':'
    if minute < 10:
        out_str += '0'
    out_str += f'{minute}'
    return out_str


print(get_out_str(out_hour, out_minute))
