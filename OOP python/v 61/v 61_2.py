class Person:
    def __init__(self):
        self.__message = "test message"


you = Person()
# print(you.__message)  # AttributeError: 'Person' object has no attribute '__message'
print(you._Person__message)  # works but don't use: Unresolved attribute reference '_Person__message' for class 'Person'
