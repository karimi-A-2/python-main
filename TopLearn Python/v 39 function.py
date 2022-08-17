# default value:
def exponent(num, power=2):
    return num ** power


print(exponent(2, 3))  # 2 * 2 * 2 = 8
print(exponent(3))  # 3 * 3 = 9
# we can leave those default parameters if we may

courses = ['python', 'kotlin', 'vuejs', 'jquery']

print(courses.pop())
print(courses)


def showFullName(first, last):
    return f"{first} {last}"


print(showFullName("Ali", "Karimi"))
# we can specify which parameter is for which argument like this:
print(showFullName(last="Ali", first="Karimi"))
