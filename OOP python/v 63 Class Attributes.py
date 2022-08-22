class User:
    activeUsersCount = 0
    allowedUsers = ['mohammad', 'milad', 'sara', 'iman']
    loggedInUsers = []

    def __init__(me, userName, userFamily):
        if userName not in User.allowedUsers:
            raise ValueError(f'{userName} can not login !!')
        me.name = userName
        me.Family = userFamily
        User.loggedInUsers.append(userName)
        User.activeUsersCount += 1
        # print(f"{me.name} logged in")

    def logout(self):
        # print(f'{self.name} logged out')
        User.activeUsersCount -= 1
        User.loggedInUsers.remove(self.name)

mohammad = User('mohammad', 'karimi')
sara = User('sara', 'moradi')

# print(User.allowedUsers)
# User.allowedUsers.append('ahmad')

# print(mohammad.allowedUsers)
# mohammad.allowedUsers.append('asgar')
# print(User.allowedUsers)

# if we change the attribute of instance it won't change the Class
# print(mohammad.allowedUsers)
# mohammad.allowedUsers = ['sina', 'bahman']
# print(User.allowedUsers)

# if we change the attribute of class it will change the instances also
print(User.allowedUsers)
print(mohammad.allowedUsers)
mohammad.allowedUsers = ['behrooz']
print(User.allowedUsers)
print(mohammad.allowedUsers)
print("------")
print(User.allowedUsers)
User.allowedUsers = ['sina', 'bahman']
print(mohammad.allowedUsers)
print(sara.allowedUsers)




# print(User.loggedInUsers)
# print(User.activeUsersCount)
#
# print(milad.allowedUsers == User.allowedUsers)
# print(milad.allowedUsers is User.allowedUsers)

# print(ali.activeUsersCount)
# print(id(ali.activeUsersCount))
#
# print(User.activeUsersCount)
# print(id(User.activeUsersCount))

