import math
n = input()
my_list = list(map(int, input().split()))
the_gcd = my_list[0]
for item in my_list:
    the_gcd = math.gcd(the_gcd, item)

newList = list()
for item in my_list:
    newList.append(item // the_gcd)
sum = 0
for i in newList:
    sum += i
print(sum)
