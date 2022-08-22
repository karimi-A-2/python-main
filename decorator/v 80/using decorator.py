def my_decorator(func):
    def wrapper():
        print('good by')  # code
        func()  # func argument call
    
    return wrapper

@my_decorator
def say_hello():
    print('hello')



say_hello()
