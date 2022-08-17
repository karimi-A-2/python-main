# key in dict
# value in dict.values()
# dict.clear()
# dict.copy()

# --> wrong
# new_dict = {}.fromkeys('name', 'test')

# --> correct
# new_dict = {}.fromkeys(["name", "family", "gender"], 'default', )
# new_dict = dict.fromkeys(["name", "family", "gender"], 'default', )

# name_value = new_user['name']  # if key does not exist raise error
# name_value = new_user.get('name')  # if key doesn't exist return None

my_dict = {
    'name': 'ali',
    'family': 'karimi',
    'age': 19,
    3: True,
}
# is_exists_1 = email in me  # wrong
is_exists_1 = 'email' in my_dict  # wrong
print(is_exists_1)

is_exists_2 = 3 in my_dict
print(is_exists_2)

is_name_exist = 'mohammad' in my_dict.values()
print(is_name_exist)

my_dict.clear()
print(my_dict)

my_dict = {
    'name': 'ali',
    'family': 'karimi',
    'age': 19,
    3: True,
}

new_dict = my_dict.copy()
print(new_dict == my_dict)
print(new_dict is my_dict)

new_user = {
    'name': 'Unknown',
    'family': 'Unknown',
    'age': 'Unknown',
    3: True,
}

new_user_2 = {}.fromkeys('name', 'test')
print(new_user_2)
# {'n': 'test', 'a': 'test', 'm': 'test', 'e': 'test'}
# because string is a list

new_user_2 = {}.fromkeys(["name", "family", "gender"], 'default', )
new_user_2 = dict.fromkeys(["name", "family", "gender"], 'default', )
print(new_user_2)
# {'name': 'default', 'family': 'default', 'gender': 'default'}

# get
name_value = new_user['name']  # if key does not exist raise error
name_value = new_user.get('name')  # if key doesn't exist return None
print(name_value)

# phone_value = new_user['phone']  # if key does not exist raise KeyError: 'phone'
phone_value = new_user.get('phone')  # if key doesn't exist return None
print(phone_value)
print(phone_value is None)
