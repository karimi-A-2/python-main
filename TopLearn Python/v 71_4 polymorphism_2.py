class Car:
    def move(self):
        raise NotImplementedError
    
    
class Benz(Car):
    def __init__(self, model):
        self.model = model
        
    def move(self):
        print(f'{self.model} is moving')


class BMW(Car):
    def __init__(self, model):
        self.model = model
    
    def move(self):
        print(f'{self.model} is moving')


class Pride(Car):
    def move(self):
        print(f'pride is moving')


sls = Benz('sls')
x4 = BMW('x4')
m141 = Pride()

sls.move()
x4.move()
m141.move()

