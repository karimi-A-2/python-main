car = ''

if car:
    print('yes')
else:
    print('no')

#  falseness => empty objects, zero, empty string, None

number = 3
print(type(number))
print(type(number) is int)
print(type(number) == int)

list1 = ['a', 'b', 'c']
list2 = list1
list3 = list(list1)
print('--------------')

print(list1 == list2)
print(list1 == list3)
print('--------------')

print(list1 is list2)
print(list1 is list3)
print('--------------')

# == -> check value
# is -> check reference

