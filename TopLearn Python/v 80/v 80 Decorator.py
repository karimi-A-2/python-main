def my_decorator(func):
    def wrapper(*args, **kwargs):  # wrapper is called wrapper
        print("this is working for me")
        func(*args, **kwargs)

    return wrapper


@my_decorator
def say_hello(name):
    print(f"hello {name}")


@my_decorator
def say_my_name(name, family):
    print(f"{name} {family}")


say_hello('mohammad')
say_my_name('mohammad', 'ordookhani')
