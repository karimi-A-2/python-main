# MRO : method resolution order
class Person:
    def __init__(self, name):
        print('Person Init')
        self.name = name
    
    def say_hello(self):
        return f'hello {self.name} in Person Class'


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

print(Admin.mro())
print(Admin.__mro__)
help(Admin)

#  |  Method resolution order:
#  |      Admin
#  |      User
#  |      Person
#  |      builtins.object
