# MRO : method resolution order
class A:
    def say_hello(self):
        print('hello python in A')


class E(A):
    pass


class C(A):
    pass
    # def say_hello(self):
    #     print('hello python in C')
    

class B(C, E):
    pass
    # def say_hello(self):
    #     print('hello python in B')


class D(B, C):
    pass
    # def say_hello(self):
    #     print('hello python in D')


item = D()
item.say_hello()
help(D)


# class D(B, C)
#  |  Method resolution order:
#  |      D
#  |      B
#  |      C
#  |      A
#  |      builtins.object
