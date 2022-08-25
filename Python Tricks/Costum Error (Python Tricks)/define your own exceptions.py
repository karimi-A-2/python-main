def validate(name):
    if len(name) < 10:
        raise ValueError


validate('ali')

"""
Traceback (most recent call last):
  File "/Users/alikarimi/Desktop/Program/python/code/Main/OOP python/Python Tricks/define your own exceptions.py", line 5, in <module>
    validate('ali')
  File "/Users/alikarimi/Desktop/Program/python/code/Main/OOP python/Python Tricks/define your own exceptions.py", line 3, in validate
    raise ValueError
ValueError
"""
# This stack trace isn’t really all that helpful
