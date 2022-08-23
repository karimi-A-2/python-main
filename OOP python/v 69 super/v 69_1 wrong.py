class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    @property
    def fullname(self):
        return f'{self.name} {self.family}'


class User(Person):
    
    # wrong: AttributeError: 'User' object has no attribute 'name'
    def __init__(self, email):
        self.email = email
        
        
ali = User('ali@gmail.com')
print(ali.fullname)
