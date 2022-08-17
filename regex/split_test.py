import re

input_str = input()
p_plus = re.compile('(\\+\\d+)')
p_minus = re.compile('(-\\d+)')
# list(map(int, input().split()))
plus_list = p_plus.findall(input_str)
print(plus_list)
minus_list = p_minus.findall(input_str)
print(minus_list)

final_str = ""
final_str += "=" + str(eval(input_str))
print(final_str)

# a = int(input())
# b = -999_999_999_999_999_999
# print(a)
# print(b)
