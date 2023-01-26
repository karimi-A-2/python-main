n = int(input())
arr = list(map(int, input().split()))


def recursive(nums):
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 1
        else:
            return 0
    sum = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            sum += recursive(nums[0:i] + nums[i + 2: len(nums)])
    return sum % (1000_000_000 + 7)


print(recursive(arr))
