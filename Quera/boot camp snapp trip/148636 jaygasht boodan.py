# todo: solve this
def permutation(arr, l, r):
    # method 1:
    # s = set()
    # maxEle = 0
    # for i in range(len(arr)):
    #     s.add(arr[i])
    #     maxEle = max(maxEle, arr[i])
    # if (maxEle != len(arr)):
    #     return False
    # if (len(s) == len(arr)):
    #     return True
    # return False
    
    # method 2:
    # length = r - l
    # temp = set()
    # for i in range(l, r):
    #     if arr[i] - 1 >= length:
    #         return False
    #     temp.add(arr[i])
    # if len(temp) != length:
    #     return False
    # for i in range(length):
    #     if i + 1 not in temp:
    #         return False
    # return True
    
    # method 3:
    length = r - l
    temp = [0 for _ in range(length)]
    for i in range(l, r):
        num = arr[i] - 1
        if num >= length:
            return False
        if temp[num] != 0:
            return False
        temp[num] = 1
    return True

    
n, q = list(map(int, input().split()))

main_list = list(map(int, input().split()))
final_ans = list()

for i in range(q):
    sign, a, b = input().split()
    a = int(a)
    b = int(b)
    if sign == '+':
        main_list[a - 1] = b
    elif sign == '?':
        if permutation(main_list, a - 1, b):
            final_ans.append('YES')
        else:
            final_ans.append('NO')
    # else:
    #     raise ValueError('should not reach this')

for i in final_ans:
    print(i)
