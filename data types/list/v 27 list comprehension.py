my_name = 'ali karimi'
name_characters_1 = [char for char in my_name]
name_characters_2 = [char.upper() for char in my_name]
print(name_characters_1)
print(name_characters_2)

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# wrong:
# even = [num if num % 2 == 0 for num in my_numbers]
even = [num for num in my_numbers if num % 2 == 0]
print(even)

odd = [num for num in my_numbers if num % 2 == 1]
print(odd)

# if_else in list comprehension:
# wrong:
# new_list = [num * 2 for num in my_numbers if num % 2 == 0 else num * 3]
new_list = [num * 2 if num % 2 == 0 else num * 3 for num in my_numbers]
print(new_list)
