str_1 = input()
pow_1 = str_1.count('0')
operation = input()
str_2 = input()
pow_2 = str_2.count('0')
out = ''
if operation == '*':
    out += '1'
    out += '0' * (pow_1 + pow_2)
elif operation == '+':
    if pow_1 == pow_2:
        out += '2'
        out += '0' * pow_1
    else:
        min_pow = min(pow_1, pow_2)
        dif_pow = abs(pow_1 - pow_2)
        out += '1'
        out += '0' * (dif_pow - 1)
        out += '1'
        out += '0' * min_pow
print(out)
