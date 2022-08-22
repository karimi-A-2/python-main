class Person:
    activeUsers = 0

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, age_value):
        if age_value >= 0:
            self._age = age_value
        else:
            # self._age = 0
            raise ValueError('age can not be negative')


ali = Person('ali', 'karimi', 19)
print(ali.get_age()) # correct
print(ali._age) # wrong
ali.set_age(-1)

