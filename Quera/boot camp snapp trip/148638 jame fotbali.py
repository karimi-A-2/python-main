n = int(input())

a = list()
b = list()
c = list()
d = list()

for i in range(n):
    a_in, b_in, c_in, d_in = list(map(int, input().split()))
    a.append(a_in)
    b.append(b_in)
    c.append(c_in)
    d.append(d_in)
    
for i in range(n):
    if (a[i] + c[i]) > (b[i] + d[i]):
        print('perspolis')
    elif (a[i] + c[i]) < (b[i] + d[i]):
        print('esteghlal')
    else:
        if (c[i]) > (b[i]):
            print('perspolis')
        elif (c[i]) < (b[i]):
            print('esteghlal')
        else:
            print('penalty')
