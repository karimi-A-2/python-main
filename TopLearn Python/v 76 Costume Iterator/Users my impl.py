class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'<name: "{self.name}", age: {self.age}>'


class UsersList:
    def __init__(self):
        self.ActiveUsers = []
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.ActiveUsers):
            person = self.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration
    
    def add_user(self, user):
        self.ActiveUsers.append(user)
        
    # def __repr__(self):
    #     return repr(self.ActiveUsers)


my_list = UsersList()
my_list.add_user(User('mohammad', 24))
my_list.add_user(User('sara', 20))
my_list.add_user(User('ali', 60))

print(my_list)
print(my_list.ActiveUsers)

for user in my_list:
    print(user)
