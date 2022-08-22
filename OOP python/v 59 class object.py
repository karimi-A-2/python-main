class User:
    shared_name = "ali"
    shared_family = "karimi"
    shared_age = 10
    
    def __init__(self, user_name, user_family):
        self.user_name = user_name
        self.user_family = user_family
    
    def show_full_name(self):
        return f"{self.user_name} {self.user_family}"


aref = User("aref", "k")
print(aref.user_name)
print(aref.user_family)
print(User.shared_name)
print(User.shared_family)
print(aref.shared_age)
