
p1, s1 = list(map(int, input().split()))
s2, p2 = list(map(int, input().split()))

if (p1 + p2) > (s1 + s2):
    print('Persepolis')
elif (p1 + p2) < (s1 + s2):
    print('Esteghlal')
else:
    if p2 > s1:
        print('Persepolis')
    elif p2 < s1:
        print('Esteghlal')
    else:
        print('Penalty')
