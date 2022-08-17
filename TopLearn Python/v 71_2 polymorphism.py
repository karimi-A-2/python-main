# poly => multi
# morph => form

class Animal:
    def make_sound(self):
        raise NotImplementedError


class Dog(Animal):
    pass
    # def make_sound(self):
    #     pass
    
    def smile(self):
        return 'dog is smiling'

class Cat(Animal):
    pass
    # def make_sound(self):
    #     pass

# but if we try to call make_sound ==> NotImplementedError will raise

dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())
