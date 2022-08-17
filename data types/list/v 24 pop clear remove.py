# list functions:

my_courses = ['python', 'kotlin', 'Ionic']
print(my_courses)

# pop()
popped = my_courses.pop()
print(my_courses)
print(f'last item is {popped}')

# pop(index)
my_courses = ['python', 'kotlin', 'Ionic']
popped = my_courses.pop(1)
print(my_courses)
print(popped)

# remove(value)
# Remove first occurrence of value.
# Raises ValueError if the value is not present.
my_courses = ['python', 'kotlin', 'Ionic', 'kotlin']
my_courses.remove('kotlin')
print(my_courses)

# clear
my_courses.clear()
print(my_courses)
