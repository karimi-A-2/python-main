n = int(input())
index_count = dict()
for i in range(n):
    name, time, sign = input().split()
    hour, minute = map(int, time.split(':'))
    point = (hour * 60) + minute
    if point in index_count:
        if sign == '+':
            index_count[point] += 1
        elif sign == '-':
            index_count[point] -= 1
    else:
        if sign == '+':
            index_count[point] = 1
        elif sign == '-':
            index_count[point] = -1
            
            
keys = list(index_count.keys())
keys.sort()

# todo: find max_point with index_count

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
