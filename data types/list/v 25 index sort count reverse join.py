# list functions:

my_courses = ['python', 'kotlin', 'Ionic', 'kotlin', 'kotlin']
print(my_courses)

# index(value, __start, __stop)
# __start(inclusive) __stop(exclusive)
# Return first index of value.
# Raises ValueError if the value is not present.
print('--------------------------------')
index_python = my_courses.index('python')
print(index_python)
index_Ionic = my_courses.index('Ionic')
print(index_Ionic)
# index_ionic = my_courses.index('ionic')  # ValueError: 'ionic' is not in list
# print(index_ionic)
# index_kotlin = my_courses.index('kotlin', 2, 3)  # ValueError: 'kotlin' is not in list
index_kotlin = my_courses.index('kotlin', 2, 4)  # index_kotlin = 3
print(index_kotlin)

# count('value')
print('--------------------------------')
my_courses = ['python', 'kotlin', 'Ionic', 'kotlin', 'kotlin']
print(my_courses.count('python'))
print(my_courses.count('sibzamini'))
print(my_courses.count('kotlin'))

# reverse()
print('--------------------------------')
my_courses = ['1', '2', 'Ionic', 'kotlin', 'kotlin']
print(my_courses)

my_courses.reverse()
print(my_courses)

# sort()
print('--------------------------------')
my_courses = ['kotlin', '2', 'Ionic', '1', 'kotlin']
print(my_courses)

my_courses.sort()
print(my_courses)

my_courses = [9, 8, 1, 2, 10, 3, 11, 5, 20]
print(my_courses)

my_courses.sort()
print(my_courses)

# join()
print('--------------------------------')
my_courses = ['kotlin', '2', 'Ionic', '1', 'kotlin']
print(my_courses)

joined_str = ' , '.join(my_courses)
print(joined_str)


