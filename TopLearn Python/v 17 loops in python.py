# for

# collection => list of numbers, list of characters in a string, range(1,5), etc

list_of_numbers = [1, 3, 8, 10, 9]


def print_line():
    print("-----------------")


for item in list_of_numbers:
    print(item)
print_line()

my_name = "ali karimi"

for a_character in my_name:
    print(a_character)
print_line()

range_of_numbers_1 = range(1, 10)  # [1, 2, 3, ... 9] (10 - 1) = 9 items
range_of_numbers_2 = range(0, 9)  # [0, 1, 2, ... 8] (9 - 0) = 9 items

for num in range_of_numbers_1:
    print(num ** 2)
print_line()
