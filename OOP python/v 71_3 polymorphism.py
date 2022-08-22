# poly => multi
# morph => form

class Animal:
    def make_sound(self):
        raise NotImplementedError


class Dog(Animal):
    
    def make_sound(self):
        return 'dog is making sound'
    
    def smile(self):
        return 'dog is smiling'

class Cat(Animal):
    
    def make_sound(self):
        return 'cat is smiling'

# so we have to implement it

dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())
