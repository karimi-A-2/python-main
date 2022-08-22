class Person:
    def __init__(self):
        self.__message__ = "test message"


you = Person()
print(you.__message__)  # ok
# print(you._Person__message__)  # AttributeError: 'Person' object has no attribute '_Person__message__'
