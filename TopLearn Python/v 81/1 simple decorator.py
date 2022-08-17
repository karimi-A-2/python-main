def decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        func(*args, **kwargs)
    
    return wrapper


@decorator
def hello(name, family):
    print(f'hello {name} {family}')


hello('ali', 'karimi')
