
n, k = list(map(int, input().split()))
my_dict = dict()

band = list()
for i in range(k):
    band.append(None)
    
for i in range(n):
    s = input()
    my_dict[s] = 1


def my_contain_first():
    for i in range(len(band)):
        if band[i] == None:
            return i
    return -1


def my_contain_last():
    for i in range(len(band) - 1, -1, -1 ):
        if band[i] == None:
            return i
    return -1
    

q = int(input())

for i in range(q):
    split = input().split()
    inst = split[0]
    arg = split[1]
    if inst == 'TAKE-OFF':
        if arg not in my_dict:
            my_dict[arg] = 4
        situation = my_dict[arg]
        if situation == 4:
            print('YOU ARE NOT HERE')
        elif situation == 3:
            print('YOU ARE LANDING NOW')
        elif situation == 2:
            print('YOU ARE TAKING OFF')
        elif situation == 1:
            index = my_contain_first()
            if index == -1:
                print('NO FREE BOUND')
            else:
                my_dict[arg] = 2
                band[index] = arg
    elif inst == 'LANDING':
        if arg not in my_dict:
            my_dict[arg] = 4
        situation = my_dict[arg]
        if situation == 1:
            print('YOU ARE HERE')
        elif situation == 2:
            print('YOU ARE TAKING OFF')
        elif situation == 3:
            print('YOU ARE LANDING NOW')
        elif situation == 4:
            index = my_contain_last()
            if index == -1:
                print('NO FREE BOUND')
            else:
                my_dict[arg] = 3
                band[index] = arg
    elif inst == 'PLANE-STATUS':
        if arg not in my_dict:
            my_dict[arg] = 4
        print(my_dict[arg])
    elif inst == 'BAND-STATUS':
        index = int(arg) - 1
        plane = band[index]
        if plane == None:
            print('FREE')
        else:
            print(plane)
    
