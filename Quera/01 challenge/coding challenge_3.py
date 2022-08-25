# todo: solve this gets 40%
A, B, m = map(int, input().split(maxsplit=2))
q = int(input())


def get_dice(a, b, m):
    x = b
    d = (x % 6) + 1
    yield d
    while True:
        x = ((a * x) + b) % m
        d = (x % 6) + 1
        yield d


dice = get_dice(A, B, m)
last_dices = []

char_mohre = {
    "R1": -1,
    "R2": -1,
    "R3": -1,
    "R4": -1,
}
for _ in range(q):
    instr = input()
    if instr[0] == 'd':
        if len(last_dices) != 0:
            print('invalid dice rolling')
            continue
        while True:
            this_dice = next(dice)
            last_dices.append(this_dice)
            if this_dice != 6:
                break
        print(*last_dices)
    elif instr[0] == 'e':
        mohre = instr.split(maxsplit=1)[1]
        if char_mohre[mohre] != -1:
            print('that is in')
        elif 6 not in last_dices:
            print('you need six')
        elif 1 in char_mohre.values():
            print('busy starting cell')
        else:
            last_dices.remove(6)
            char_mohre[mohre] = 1
            print(1)
    elif instr[0] == 'm':
        _, mohre, step = instr.split(maxsplit=2)
        step = int(step)
        if step not in last_dices:
            print('invalid move')
        elif char_mohre[mohre] == -1:
            print('it is not in')
        elif char_mohre[mohre] + step > 40:
            print('you can not move')
        elif (char_mohre[mohre] + step) in char_mohre.values():
            print('destination is busy')
        else:
            last_dices.remove(step)
            char_mohre[mohre] += step
            print(char_mohre[mohre])
    elif instr[0] == 'g':
        last_dices.clear()
    else:
        raise ValueError(f'{instr} is invalid')
    