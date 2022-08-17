# iterable is an object that chan be converted to iterator
# iterator is

# iterate

num_list = [1, 2, 3]
color = ('red', 'green', 'blue')
num_set = {1, 2, 3}

for num in num_list:
    print(num)
    
# next()
# iter()
# iterable => iter() => iterator

num_list_iterator = iter(num_list)
print(num_list_iterator)
print(type(num_list_iterator))

print(next(num_list_iterator))  # 1
print(next(num_list_iterator))  # 2
print(next(num_list_iterator))  # 3
print(next(num_list_iterator))  # error --> StopIteration
