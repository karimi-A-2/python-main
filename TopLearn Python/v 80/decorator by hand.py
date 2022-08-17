def my_decorator(func):
    def wrapper():
        print('good by')  # code
        func()  # func argument call
    
    return wrapper


def say_hello():
    print('hello')


say_hello_wrapped = my_decorator(say_hello)
say_hello_wrapped()
