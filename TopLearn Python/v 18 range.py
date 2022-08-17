my_numbers = range(1, 10)
print(my_numbers)
string_rep: str = my_numbers.__repr__()
print(string_rep)

result = list(my_numbers)
print(result)

print(list(range(1, 4)))

print(list(range(5)))
print(list(range(1, 10, 3))) # [1, 4, 7]
print(list(range(10, 1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# for num in range(5):
for num in range(1, 6):
    print("*" * num)

count = 1
my_length = 5
for i in range(count):
    for num in range(1, my_length + 1, +1):  # increasing ==> step = +1
        #            [1 .... my_length]
        print("*" * num)
    print("*" * (my_length + 1))
    for num in range(my_length, 1 - 1, -1):  # decreasing ==> step = -1
        #            [my_length .... 1]
        print("*" * num)
