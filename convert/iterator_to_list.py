from typing import Iterator

if __name__ == '__main__':
    
    n = int(input())
    arr: Iterator[int] = map(int, input().split())
    
    # there are three cases to convert iterator to list
    
    # 1:
    arr = list(arr)
    
    # 2:
    arr = [i for i in arr]
    
    # 3:
    arr = [*arr]
