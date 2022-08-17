n, m, c = map(int, input().strip().split(maxsplit=2))
num_dict = dict()
nums = list(map(int, input().strip().split()))
requests = list(map(int, input().strip().split()))


def operate():
    for i in range(n):
        if nums[i] not in num_dict:
            num_dict[nums[i]] = i + 1
        else:
            key = ((nums[i] + c - 1) % n) + 1  # be careful
            # wrong: nums[i] = 3    ==> (3 + 2) % 5 = 0
            # correct: nums[i] = 3  ==> ((3 + 2 - 1) % 5) + 1 = 5
            while key in num_dict:
                key = ((key + c - 1) % n) + 1
                if key == nums[i]:
                    return False
            num_dict[key] = i + 1
    return True


if operate():
    reversed_dict = {v: k for k, v in num_dict.items()}
    out_list = [reversed_dict[num] for num in requests]
    print(*out_list)
else:
    print('Impossible')
    
"""
5 5 2
5 1 5 2 5
1 2 3 4 5

5 1 2 4 3

5 5 2
5 1 5 2 5
1 1 1 1 1

5 5 1
5 1 5 2 5
1 2 3 4 5

6 6 3
2 2 5 5 5
1 2 3 4 5

2 2 1
1 1
1 2

"""
