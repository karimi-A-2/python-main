class Person:
    activeUsers = 0
    
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
    
    def show_full_name(self):
        return f'{self.name} {self.family}'


class User(Person):
    pass


ali = User('ali', 'karimi', 19)
print(ali.name)
print(ali.show_full_name())

print(User.activeUsers)
