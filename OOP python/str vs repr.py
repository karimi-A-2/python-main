class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"Person(name: {self.name})"
    
    def __str__(self) -> str:
        return f"my name is '{self.name}'"


person = Person('ali')
print(person)
