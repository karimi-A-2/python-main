def sum_all_numbers(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total


# arguments will store in *args as Tuple
print(sum_all_numbers(1, 2, 3))

numbers = [1, 2, 3, 4, 5, 6]
# wrong:
# print(sum_all_numbers(numbers))  # ([1,2,3,4,5,6],)  Tuple of list
# correct: put * before list name to unpack it
print(sum_all_numbers(*numbers))  # (1,2,3,4,5,6)


def sum_all_numbers_2(name, *args):
    print(name)
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_numbers_2('second', 4))
print(sum_all_numbers_2('third', 1, 5, 6, 9))


def showUserInfo(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


showUserInfo(name="mohammad", family="orodookhani",
             age=23, email="moh96ordo@gmail.com")


def display_names(name, family):
    print(f"name is {name} and family is {family}")


person = {"name": "sara", "family": "moradi"}

# display_names(person)     # TypeError: display_names() missing 1 required positional argument: 'family'
display_names(*person)      # name is name and family is family         => *    --> unpack keys
display_names(**person)     # name is sara and family is moradi         => **   --> upack keys value
# *person = "name", "family"
# **person = "name"="sara", "family"="moradi"


# parameters
# *args
# default parameters
# **kwargs

def display_info(a, b, *args, defPara="defalut", **kwargs):
    return [a, b, args, defPara, kwargs]


print(display_info(1, 2, 6, first_name="mohammad", last_name="ordookhani"))
# [1, 2, (6,), 'defalut', {'first_name': 'mohammad', 'last_name': 'ordookhani'}]
# [a, b, args, defPara  , kwargs]
