# find the runner-up score
from typing import Iterator

if __name__ == '__main__':
    n = int(input())
    # arr: Iterator[int] = map(int, input().split())
    # arr = list(arr)
    arr = list(map(int, input().split()))
    max_score = max(arr)
    while max(arr) == max_score:
        arr.remove(max(arr))
    runner_up = max(arr)
    print(runner_up)

"""
6
1 3 2 3 3 4
out: 3
"""
