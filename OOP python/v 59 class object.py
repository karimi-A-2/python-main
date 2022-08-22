class User:
    userName = "ali"
    userFamily = "karimi"
    age = 10

    def __init__(self, userName, userFamily):
        self.userName = userName
        self.userFamily = userFamily


    def showFullName(self):
        return f"{self.userName} {self.userFamily}"


aref = User("aref", "k")
print(aref.userName)
print(aref.userFamily)
print(User.userName)
print(User.userFamily)
print(aref.age)
