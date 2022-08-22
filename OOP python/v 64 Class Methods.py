class User:
    activeUsers = 0

    def __init__(self, name, family):
        self.name = name
        self.family = family
        User.activeUsers += 1
        print(f'{self.name} logged in')

    def logout(self):
        User.activeUsers -= 1
        print(f'{self.name} has logged out')

    @classmethod
    def getActiveUsersCout(cls):
        print(f'there are currently {cls.activeUsers} active users')

    @classmethod
    def from_string(cls, string_data):
        name, family = string_data.split(',')
        return cls(name, family)

# print(User.activeUsers)
# me = User('mohammad', 'karimi')
# print(User.activeUsers)

# User.getActiveUsersCout()
# me = User('mohammad', 'karimi')
# User.getActiveUsersCout()

print(dict.fromkeys([1, 2, 3], 'hello'))
new_instance = User.from_string('ali,karimi')
print(new_instance.name, new_instance.family)
