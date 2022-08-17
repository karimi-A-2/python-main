from functools import wraps


# decorator factory
def check_str_length(length):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(name):
            if len(name) > length:
                raise ValueError("name is too long")
            else:
                func(name)
            return func  # todo: why this line?
        
        return wrapper
    
    return inner_decorator


@check_str_length(5)
def show_name(name):
    print(f'hello {name}')


show_name('ali karimi')
print(show_name.__name__)
