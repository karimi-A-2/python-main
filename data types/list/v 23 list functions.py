# list functions:

my_courses = ['python', 'kotlin', 'ionic']
print(my_courses)

my_courses.append('Java')
print(my_courses)

# # wrong: error
# my_courses.append('JQuery', 'Vue js')  # TypeError: append() takes exactly one argument (2 given)
# print(my_courses)

# wrong: nested list
my_courses.append(['JQuery', 'Vue js'])
print(my_courses)

# correct: extend
my_courses.extend(['A', 'B'])
print(my_courses)

my_courses = ['python', 'kotlin', 'ionic']
my_courses.insert(0, '0')
print(my_courses)

my_courses = ['python', 'kotlin', 'ionic']
my_courses.insert(1, '1')
print(my_courses)

my_courses = ['python', 'kotlin', 'ionic']
my_courses.insert(-1, '-1')
print(my_courses)

my_courses = ['python', 'kotlin', 'ionic']
my_courses.insert(-2, '-2')
print(my_courses)

# my_courses_2 = [['JQuery', 'Vue js']]
