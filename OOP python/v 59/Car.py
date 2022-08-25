class Car:
    
    def __init__(self, name, numberOfDoors, color):  # Dunder method (double underline method)
        self.name = name
        self.numberOfDoors = numberOfDoors
        self.color = color
    
    def show_info(self):  # instance method
        return f"car name is {self.name} & car color is {self.color}"
    
    @classmethod
    def foo(cls):
        pass


Car.foo()

benz = Car("sls", 2, "red")
benz_2 = Car("test", 2, "yellow")


print(benz.show_info())
print(benz_2.show_info())
print(Car.show_info(benz_2))  # ? --> Car is an Object

# everything in python is an object
