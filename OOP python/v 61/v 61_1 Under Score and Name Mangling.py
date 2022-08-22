# name      => normal
# _name     => protected(private) but accessible
# __name    => name mangling
# __name__  => normal like built in

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


me = User("ali")
print(me.userName)  # normal attribute
me.login('123')
print(me._password)  # Access to a protected member _password of a class
# print(me.__message)  # AttributeError: 'User' object has no attribute '__message'
print(dir(me))
print(me._User__message)
