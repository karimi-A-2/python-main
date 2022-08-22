from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'func name is: {func.__name__}')
        return func(*args, **kwargs)
    
    return wrapper


@decorator
def hello(name, family):
    print(f'hello {name} {family}')


hello('ali', 'karimi')
print(hello.__name__)  # hello
