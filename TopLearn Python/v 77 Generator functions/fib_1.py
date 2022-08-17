# do not run this: it will cause memory pressure
# and Process finished with exit code 137 (interrupted by signal 9: SIGKILL)
# because it uses list to store data rather than generating.
def fib_list(max):  # 10
    nums = []  # [1,1]
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


fib_list(1000000)
