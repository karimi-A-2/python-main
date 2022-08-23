class User:
    activeUsersCount = 0
    
    def __init__(self, name, family):
        self.name = name
        self.family = family
        User.activeUsersCount += 1
        print(f'{self.name} logged in')
    
    def logout(self):
        User.activeUsersCount -= 1
        print(f'{self.name} has logged out')
    
    @classmethod
    def print_active_users_count(cls):
        print(f'there are currently {cls.activeUsersCount} active users')
    
    @classmethod
    def from_string(cls, string_data):
        name, family = string_data.split(',', 1)
        return cls(name, family)


print(User.activeUsersCount)
ali = User('ali', 'karimi')
print(User.activeUsersCount)

User.print_active_users_count()
mohammad = User('mohammad', 'mohammadian')
User.print_active_users_count()

print(dict.fromkeys([1, 2, 3], 'hello'))
new_instance = User.from_string('ali,karimi')
print(new_instance.name, new_instance.family)
