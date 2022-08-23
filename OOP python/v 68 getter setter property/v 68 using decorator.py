class Person:
    
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    @property
    def age(self):  # replacement of getter
        return self._age
    
    @age.setter  # replacement of setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('age can not be negative')
    
    @property  # we can also define properties like this (read only property)
    def full_name(self):
        return f'{self.name} {self.family}'


ali = Person('ali', 'karimi', 19)
print(ali.age())  # TypeError: 'int' object is not callable
print(ali.age)  # this is property call the getter function
ali.age = 10  # this will call setter
ali.age = -1  # this will call setter and raise ValueError
print(ali.full_name)
