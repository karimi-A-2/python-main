# WARNING: This implementation contains a bug
class BuggyCountedObject:
    num_instances = 0
    
    def __init__(self):
        self.num_instances += 1  # !!!


first = BuggyCountedObject()
print(first.num_instances)
second = BuggyCountedObject()
print(second.num_instances)
third = BuggyCountedObject()
print(third.num_instances)
print(BuggyCountedObject.num_instances)
