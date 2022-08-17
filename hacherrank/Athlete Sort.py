import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    
    n = int(nm[0])
    # n = 5
    
    m = int(nm[1])
    # m = 3
    
    arr = []
    # arr = [[10, 2, 5],
    #        [7, 1, 0],
    #        [9, 9, 9],
    #        [1, 23, 12],
    #        [6, 5, 9]]
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())
    # k = 2
    
    out_indexes = []
    indexes = list(range(len(arr)))
    while len(indexes) > 0:
        min_val_index = indexes[0]
        for i in indexes:
            if arr[i][k] < arr[min_val_index][k]:
                min_val_index = i
        out_indexes.append(min_val_index)
        indexes.remove(min_val_index)
    for i in out_indexes:
        for element in arr[i]:
            print(element, end=" ")
        print()
