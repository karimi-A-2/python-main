# list slicing => to make a copy of list
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_numbers)
print(f'length = {len(my_numbers)}')

# some_list[start:end:step]
# Start(inclusive)
# Stop(exclusive)
selected_numbers = my_numbers[1:7:1]
print(selected_numbers)

print(my_numbers[1:7:2])
print(my_numbers[1::2])
print(my_numbers[0::2])
print(my_numbers[-3:])
print(my_numbers[2:])  # important
print(my_numbers[2:-1])  # important
