class Person:
    def __init__(self, name):
        print('Person Init')
        self.name = name
    
    def say_hello(self):
        return f'hello {self.name} in Person Class'
    
    def say_goodbye(self):
        return f'goodbye {self.name} just in Person Class'


class User:
    def __init__(self, name):
        print('User Init')
        self.name = name
    
    def say_hello(self):
        return f'hello {self.name} in User Class'


class Admin(User, Person):
    def __init__(self, name):
        print('Admin Init')
        super().__init__(name)


ali = Admin('ali')
print(ali.name)
print(ali.say_hello())
print(ali.say_goodbye())

# print(isinstance(ali, Admin))
# print(isinstance(ali, User))
# print(isinstance(ali, Person))



