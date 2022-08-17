from random import choice


def greet(person):
    def get_mood():
        msg = choice(('hello there ', 'go away ', 'goodbye '))
        res = msg + person
        return res

    return get_mood


res = greet('mohammad')

print(res())
