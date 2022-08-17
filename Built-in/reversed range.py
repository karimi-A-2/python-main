# bad practice
for i in range(5 - 1, -1, -1):  # don't use this
    print(i)
# good practice
for i in reversed(range(5)):
    print(i)
