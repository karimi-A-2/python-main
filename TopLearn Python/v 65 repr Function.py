class User:
    activeUsers = 0

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.family} is {self.age}'


ali = User('ali', 'karimi', 19)
print(ali)
