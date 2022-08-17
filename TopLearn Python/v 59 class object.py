class User:
    userName = "ali"
    userFamily = "karimi"
    age = 10

    def showFullName(self):
        return f"{self.userName} {self.userFamily}"

    def __init__(self, userName, userFamily):
        self.userName = userName
        self.userFamily = userFamily


alikarimi = User("ali", "karimi")
alikarimi.age = 10
print(alikarimi.age)
