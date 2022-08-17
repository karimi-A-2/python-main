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

# make_soutnd is not called so no error and works ok

dog = Dog()
# cat = Cat()
print(dog.smile())
# print(cat.make_sound())
