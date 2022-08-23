class Person:
    
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    
    def get_age(self):
        return self._age
    
    
    def set_age(self, age_value):
        if age_value >= 0:
            self._age = age_value
        else:
            raise ValueError('age can not be negative')


    def get_full_name(self):
        return f"{self.name} {self.family}"


ali = Person('ali', 'karimi', 19)
print(ali.get_age())  # correct
print(ali._age)  # wrong => Access to a protected member _age of a class
ali.set_age(10)  # this will call setter
ali.set_age(-1)  # ValueError: age can not be negative
print(ali.get_full_name())
