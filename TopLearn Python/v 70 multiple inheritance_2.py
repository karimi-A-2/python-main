class Person:
    def __init__(self, name):
        print('Person Init')
        self.__name = name
    
    def say_hello(self):
        return f'hello {self._Person__name} in Person Class'
    
    def say_goodbye(self):
        return f'goodbye {self._Person__name}'


class User:
    def __init__(self, name):
        print('User Init')
        self.__name = name
    
    def say_hello(self):
        return f'hello {self._User__name} in User Class'


class Admin(Person, User):
    def __init__(self, name):
        print('Admin Init')
        print(f'got name is {name}')
        # super().__init__(name)
        User.__init__(self, 'user name')
        Person.__init__(self, 'person name')


ali = Admin('ali')
print(ali.say_hello())

# print(isinstance(ali, Admin))
# print(isinstance(ali, User))
# print(isinstance(ali, Person))

print(ali._Person__name)
print(ali._User__name)

print(ali.say_goodbye())
print(ali.say_hello())

