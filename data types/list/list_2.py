a = [0 for i in range(10)]
print(a)

# wrong: error
# a[:5] -= 1

# wrong: does not what i want to do
# for i in a[:5]:
#     i -= 1

# OK
for i in range(0, 5):
    a[i] -= 1
    
print(a)