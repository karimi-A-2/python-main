def compute_left_to_right(a, b):
    a_point = 0
    b_point = 0
    while not (b_point == len(b) or
               a_point == len(a)):
        if a[a_point] == b[b_point]:
            b_point += 1
        a_point += 1
    if b_point == len(b):
        return True
    else:
        return False


def compute_right_to_left(a, b):
    a_point = len(a) - 1
    b_point = 0
    while not (b_point == len(b) or
               a_point == -1):
        if a[a_point] == b[b_point]:
            b_point += 1
        a_point -= 1
    if b_point == len(b):
        return True
    else:
        return False


n = int(input())
for i in range(n):
    a = input()
    b = input()
    if compute_left_to_right(a, b) or compute_right_to_left(a, b):
        print('YES')
    else:
        print('NO')
