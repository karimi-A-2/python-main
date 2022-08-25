def test():
    inner()
    
    
def inner():
    for i in range(3):
        yield i


for num in test():
    print(num)
