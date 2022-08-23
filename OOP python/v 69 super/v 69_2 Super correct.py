class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    @property
    def fullname(self):
        return f'{self.name} {self.family}'


class User(Person):
    
    # correct:
    def __init__(self, name, family, email):
        # Person.__init__(self, name, family)
        super().__init__(name, family)
        self.email = email


ali = User('ali', 'karimi', 'ali@gmail.com')
print(ali.fullname)
print(ali.email)
