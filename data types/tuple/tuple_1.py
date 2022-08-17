my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(type(my_tuple))

my_tuple = ("apple")  # wrong: str
print(my_tuple)
print(type(my_tuple))

my_tuple = ("apple",)  # correct: tuple
print(my_tuple)
print(type(my_tuple))

# we have duplicate because it is indexed
this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)
print("this tuple[0]:", this_tuple[0])
print("this tuple[4]:", this_tuple[4])
