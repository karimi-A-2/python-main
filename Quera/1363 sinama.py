# todo: solve this:
from typing import List

n = int(input())
arr = []
for i in range(n):
    arr.append([char for char in input()])

new_arr: List[List[str]]


def get_counts():  # takes so much time 1418 ms !! too much
    soal_khial = 0
    tajob_khial = 0
    for ii in range(i - 1, i - 1 + 3):
        if not (0 <= ii < n):
            continue
        for jj in range(j - 1, j - 1 + 3):
            if not (0 <= jj < n):
                continue
            if ii == i and jj == j:
                continue
            if arr[ii][jj] == '?':
                soal_khial += 1
            elif arr[ii][jj] == '!':
                tajob_khial += 1
    return soal_khial, tajob_khial


def get_new_char(char, soal_khial, tajob_khial):
    new_char = char
    if char == '_':
        if soal_khial + tajob_khial == 3:
            if soal_khial > tajob_khial:
                new_char = '?'
            elif soal_khial < tajob_khial:
                new_char = '!'
    elif char == '?' or char == '!':
        sum_khial = soal_khial + tajob_khial
        if not (2 <= sum_khial <= 3):
            new_char = '_'
        elif char == '!' and soal_khial > tajob_khial:
            new_char = '?'
        elif char == '?' and soal_khial < tajob_khial:
            new_char = '!'
    return new_char


for k in range(1000):
    new_arr = []
    for i in range(n):
        new_inner_arr = []
        for j in range(n):
            char = arr[i][j]
            if char == '#':
                new_inner_arr.append('#')
                continue
            soal_khial, tajob_khial = get_counts()
            new_char = get_new_char(char, soal_khial, tajob_khial)
            new_inner_arr.append(new_char)
        new_arr.append(new_inner_arr)
    if new_arr == arr:
        break
    arr = new_arr
    
soal_sum = 0
tajob_sum = 0

for row in arr:
    soal_sum += row.count('?')
    tajob_sum += row.count('!')

print(soal_sum)
print(tajob_sum)
