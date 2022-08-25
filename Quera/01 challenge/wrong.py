def value(s):
    res = 0
    for i in range(len(s)):
        res += ord(s[i]) - ord(s[0])
    return res


print(value('bmin'))
