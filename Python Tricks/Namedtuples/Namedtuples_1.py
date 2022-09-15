# tuples are immutable
import json

tup = ('hello', object(), 42)
print(tup)
print(tup[2])
tup[2] = 23  # TypeError: 'tuple' object does not support item assignment

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
'color mileage'.split()
Car = namedtuple('Car', ['color', 'mileage'])
Car = namedtuple('Car', [
    'color',
    'mileage',
])

my_car = Car('red', 3812.4)
my_car.color
my_car.mileage
my_car[0]
tuple(my_car)
color, mileage = my_car
print(color, mileage)
print(*my_car)
my_car

my_car.color = 'blue'

ElectricCar = namedtuple(
    'ElectricCar', Car._fields + ('charge',))

ElectricCar('red', 1234, 45.0)
ElectricCar(color='red', mileage=1234, charge=45.0)

my_car._asdict()
json.dumps(my_car._asdict())

my_car._replace(color='blue')

Car._make(['red', 999])