class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


validate('jane')

"""
Traceback (most recent call last):
  File "/Users/alikarimi/Desktop/Program/python/code/Main/OOP python/Python Tricks/better aproach.py", line 10, in <module>
    validate('jane')
  File "/Users/alikarimi/Desktop/Program/python/code/Main/OOP python/Python Tricks/better aproach.py", line 7, in validate
    raise NameTooShortError(name)
__main__.NameTooShortError: jane
"""
