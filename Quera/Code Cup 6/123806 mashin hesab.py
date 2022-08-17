# todo: complete this
import re

input_str = input()
# +9+7+8+11-1-10-20-11
p_plus = re.compile('(\\+\\d+)')
p_minus = re.compile('(-\\d+)')


plus_list_str = p_plus.findall(input_str)
# print(plus_list_str)
plus_list = list(map(int, plus_list_str))
# print(plus_list)
sorted_plus = sorted(plus_list)
# print(sorted_plus)
# [7, 8, 9, 11]

minus_list_str = p_minus.findall(input_str)
# print(minus_list_str)
minus_list = list(map(int, minus_list_str))
# print(minus_list)
sorted_minus = sorted(minus_list)
# print(sorted_minus)
# [-20, -11, -10, -1]

out_str = ""
if len(sorted_plus) == len(sorted_minus):
    for i in range(0, len(sorted_plus)):
        out_str += "+"
        out_str += str(sorted_plus[len(sorted_plus) - 1 - i])
        out_str += str(sorted_minus[len(sorted_minus) - 1 - i])
elif len(sorted_plus) > len(sorted_minus):
    for i in range(0, len(sorted_minus)):
        out_str += "+"
        out_str += str(sorted_plus[len(sorted_plus) - 1 - i])
        out_str += str(sorted_minus[len(sorted_minus) - 1 - i])
    balanced_value = eval(out_str)

out_str = out_str + "=" + str(eval(input_str))
print(out_str, end="")

# a = int(input())
# b = -999_999_999_999_999_999
# print(a)
# print(b)
