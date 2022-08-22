from random import choice


def greet(person):
    def get_mood():
        msg = choice(('hello there ', 'go away ', 'goodbye '))
        return msg
    
    result = get_mood() + person
    return result


print(greet("mohammad"))
