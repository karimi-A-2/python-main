class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
    
    def __repr__(self) -> str:
        return f'{self.name} {self.family}'
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        # return other
        return self.age + other.age
    
    def __mul__(self, other):
        return self.age * other.age
    
    def __truediv__(self, other):
        return self.age / other.age
    
    def __floordiv__(self, other):
        return self.age // other.age
    
    def __pow__(self, power, modulo=None):
        return self.age ** power

        
person_1 = Person('ali', 'karimi', 10)
print(person_1)

# if we don't override __len__(self) method
# TypeError: object of type 'Person' has no len()

# if we override __len__ but pass and return None
# TypeError: 'NoneType' object cannot be interpreted as an integer

# if we return self.age it will print age
print(len(person_1))

person_2 = Person('aref', 'moradi', 20)
print(person_1 + person_2)

# print(person_1 + {'name': ['ali', 'aref']})
# AttributeError: 'dict' object has no attribute 'age'
# if we don't override __add__(self, other):
# TypeError: unsupported operand type(s) for +: 'Person' and 'Person'

print(person_1 + person_2)  # __add__
print(person_1 * person_2)  # __mul__
print(person_1 / person_2)  # __truediv__
print(person_1 // person_2)  # __floordiv__
print(person_1 ** 3)  # __pow__
# and ...
