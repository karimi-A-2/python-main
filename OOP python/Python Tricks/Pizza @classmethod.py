class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
        # return Pizza(['mozzarella', 'tomatoes'])  # not recommended
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


print(Pizza.margherita())
print(Pizza.prosciutto())
