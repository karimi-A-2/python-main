class MyClass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
print(MyClass.method())  # wrong
print(MyClass.method(obj))  # ok but not recommended
