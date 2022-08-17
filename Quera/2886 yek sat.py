
hour1, minute1 = list(map(int, input().split()))

if hour1 != 0:
    hour2 = 12 - hour1
else:
    hour2 = 0

if minute1 != 0:
    minute2 = 60 - minute1
else:
    minute2 = 0

print('%.2d:%.2d' % (hour2, minute2))

# error:
# print('{:.2d}:{:.2d}'.format(hour2, minute2))
# print(f'{hour2:.2d}:{minute2:.2d}')
