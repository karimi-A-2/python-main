numbers = [1, 5, 8, 4, 6, 2]
print(numbers)

# numbers.sort()
# print(numbers)


result = sorted(numbers, reverse=True)
print(result)

print(numbers)

users = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'taha', 'family': 'ordookhani', 'age': 40},
    {'name': 'ali', 'family': 'ordookhani', 'age': 30},
    {'name': 'sara', 'family': 'ordookhani', 'age': 80}
]

sorted_1 = sorted(users, key=lambda user: user['age'])
for item in sorted_1:
    print(item)
    
print('---------')

sorted_2 = sorted(users, key=lambda user: user['age'], reverse=True)
for item in sorted_2:
    print(item)

