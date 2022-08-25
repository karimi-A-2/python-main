# todo: solve this
# n = int(input())
n = 12
glob_normal = [i + 1 for i in range(n)]
sum_glob_1 = n * (n + 1) // 2
sum_glob_2 = n * (n + 1) * (2 * n + 1) // 6
sum_glob_3 = (n ** 2) * ((n + 1) ** 2) // 4


class CostumeError(ValueError):
    
    def __init__(self, list_) -> None:
        super().__init__()
        self.list_ = list_


output = []
sub_vector = []


def recurrence(count, sum_, last):
    global output, sub_vector, sum_glob_1, sum_glob_2, sum_glob_3, glob_normal
    if count == 0 and sum_ == 0:
        if sub_vector == glob_normal:
            return
        sum_nums_2 = 0
        sum_nums_3 = 0
        for item in sub_vector:
            sum_nums_2 += item ** 2
            sum_nums_3 += item ** 3
        if (sum_nums_2 == sum_glob_2 and
                sum_nums_3 == sum_glob_3):
            raise CostumeError(list(sub_vector))
        
        # output.append(list(sub_vector))
        return
    
    if count <= 0 or sum_ <= 0:
        return
    
    for num in range(last, sum_glob_1):
        sub_vector.append(num)
        recurrence(count - 1, sum_ - num, num)
        sub_vector.pop()


# recurrence(3, 9, 1)
# for item in output:
#     print(*item)

try:
    recurrence(n, sum_glob_1, 1)
except CostumeError as err:
    print(*err.list_)
else:
    print(-1)

# 1
# -1

# 2
# -1

# 3
# -1

# 4
# -1

# 5
# -1

# 6
# -1

# 7
# -1

# 8
# 2 2 2 3 6 7 7 7

# 9
# 1 1 5 5 5 6 6 6 10

# 10
# 1 1 4 5 6 6 6 7 8 11

# 11
# 1 1 4 5 5 6 7 8 8 9 12

# 12
# 1 1 3 6 6 6 7 8 8 8 11 13
