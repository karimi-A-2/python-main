class Person:
    classAttribute = "test value"
    
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
    
    def show_full_name(self):
        return f"{self.name} {self.family}"
    
    @classmethod
    def show_class_attribute(cls):
        return Person.classAttribute


class User(Person):
    pass


mohammad = Person('mohammad', 'ordookhani', 24)
sara = User('sara', 'moradi', 24)
print(mohammad.name)
print(sara.show_full_name())
print(User.classAttribute)
print(User.show_class_attribute())
print(sara.name)
