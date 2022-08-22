from functools import wraps


def show_decorator(is_show):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if is_show:
                func(*args, **kwargs)
            else:
                raise ValueError("you don't have permission!")
        
        return wrapper
    
    return inner_decorator


@show_decorator(True)
def go_to_admin_page(name, family):
    print(f'hello {name} {family} this is admin page')


go_to_admin_page('ali', 'karimi')
