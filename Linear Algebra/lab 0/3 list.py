i = 1
f = 1.1
s = "salam!"
l = [1, 2, 3, 4]
print(l)
l = [i, f, s, 2]
l
l = l + [True]
l += [False]
l
l = l + [1, 3, 45]
l
len(l)
l.append('hi')
l
l.insert(0, 100)
l
l.insert(2, 111)
l
111 in l
112 in l
112 not in l
l.extend(['a', 'b', 'c'])
l
l += ['a', 'b', 'c']
l
l.pop()
l
k = l.pop(2)
l
k
l = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
l[0]
l[1]
l[5]
l[-1]
l[-2]
l[1:5]
l[10:1]
l[1:10]
l[1:10:2]
l[::3]
l[10:1]
l[10:1:-1]
l[::-1]
l = [4, 1, 7, 2, 0]
l[4] = 100
print(l)
l[1] = 100
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l = [4, 1, 7, 2, 0]
t = l
l[1] = 100
print(l)
print(t)
l = [4, 1, 7, 2, 0]
t = l[:]
l[1] = 100
print(l)
print(t)
