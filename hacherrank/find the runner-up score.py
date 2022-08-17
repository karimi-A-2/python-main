# find the runner-up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
max_score = runner_up = -200
for i in arr:
    # print("i:", i)
    if i > max_score and i > runner_up:
        runner_up = max_score
        max_score = i
    elif runner_up < i < max_score:
        runner_up = i
    else:
        pass
    # print("max_score:", max_score)
    # print("runner_up:", runner_up)
print(runner_up)
