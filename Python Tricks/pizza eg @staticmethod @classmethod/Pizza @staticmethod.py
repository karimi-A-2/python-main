import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients
    
    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')
    
    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):  # independent
        return r ** 2 * math.pi


print(repr(Pizza(9, ['mushrooms'])))
p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza.circle_area(4))
