n = int(input())
answer_sheet = input()

ans_list = list()
for char in answer_sheet:
    if char == 'A':
        ans_list.append('#OOO')
    elif char == 'B':
        ans_list.append('O#OO')
    elif char == 'C':
        ans_list.append('OO#O')
    elif char == 'D':
        ans_list.append('OOO#')
    else:
        raise ValueError(f'{char} is undefined')
empty = 'OOOO'

k = int(input())
final_list = list()
for i in range(k):
    sum_score = 0
    for j in range(n):
        this_answer = input()
        if this_answer == empty:
            continue
        elif this_answer == ans_list[j]:
            sum_score += 3
        else:
            sum_score -= 1
    final_list.append(sum_score)

for item in final_list:
    print(item)
