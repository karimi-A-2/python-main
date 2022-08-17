# MRO : method resolution order
class A:
    def say_hello(self):
        print('hello python in A')


class B(A):
    def say_hello(self):
        print('hello python in B')


class C(A):
    def say_hello(self):
        print('hello python in C')


class D(B, C):
    pass
    # def say_hello(self):
    #     print('hello python in D')


item = D()
item.say_hello()
help(D)

# first check in class D to see if it has say_hello()
# if not check in B then C then A

# class D(B, C)
#  |  Method resolution order:
#  |      D
#  |      B
#  |      C
#  |      A
#  |      builtins.object
