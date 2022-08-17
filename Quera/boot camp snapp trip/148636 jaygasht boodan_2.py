def is_permutation(arr, left, right):
    # s = set()
    # maxEle = 0
    # for index in range(len(arr)):
    #     s.add(arr[index])
    #     maxEle = max(maxEle, arr[index])
    # if (maxEle != len(arr)):
    #     return False
    # if (len(s) == len(arr)):
    #     return True
    # return False
    length = right - left
    temp = set()
    for index in range(left, right):
        if arr[index] > length:
            return False
        temp.add(arr[index])
    if len(temp) != length:
        return False
    # for index in range(length):
    #     if index + 1 not in temp:
    #         return False
    return True


if __name__ == '__main__':
    
    n, q = list(map(int, input().split()))
    
    main_list = list(map(int, input().split()))
    final_ans = list()
    
    for i in range(q):
        split = input().split()
        a = int(split[1])
        b = int(split[2])
        if split[0] == '+':
            main_list[a - 1] = b
        elif split[0] == '?':
            if is_permutation(main_list, a - 1, b):
                final_ans.append('YES')
            else:
                final_ans.append('NO')
        else:
            raise ValueError('should not reach this')
    
    for i in final_ans:
        print(i)
