my_colors = ['red', 1.2,  'green', 'blue', 'yellow', 'gray', 'orange', 4]
for color in my_colors:
    if type(color) == str:
        print(f'color is :{color}')
    else:
        print(f'{color} is not a color')

print('-------------')

index = 0
while index < len(my_colors):
    print(my_colors[index])
    index += 1
