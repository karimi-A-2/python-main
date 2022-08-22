class User:
    def __init__(self, userName):
        self.userName = userName
        self._password = "123"
        self.__message = "i love python"

    def login(self, gotPassword):
        if self._password == gotPassword:
            print("login user")
        else:
            print("you are not logged in")

class Person:
    def __init__(self):
        self.__message = "test message"


you = Person()
print(you._Person__message)

me = User("ali")
print(me.userName)
me.login('123')
# print(me.__message) # error
print(dir(me))
print(me._User__message)
