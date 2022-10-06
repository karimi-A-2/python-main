i = 12
b = 1
if i == 12:
    b = 2
print(b)

i = 12
if i == 10:
    print('YES')
    print('i equals 10')
else:
    print('NO')
    print('i is not equal to 10')

i = 11
b = 'salam'
if i == 12:
    print('Twelve')
elif i == 11 and b == 'hi':
    print('Eleven-hi')
elif i > 10 and b == 'salam':
    print('SALAAAMM!!')
else:
    print('None')

i = 10
while i > 0:
    print(i * i)
    i -= 2

l = [10, 20, 30, 40.2, 'salam']
for k in l:
    print(k)

p = [1, 2, 3]
q = ['One', 'Two', 'Three']
for i in range(len(p)):
    print(p[i], q[i])

for k in range(2, 20):
    print(k, k * k)
