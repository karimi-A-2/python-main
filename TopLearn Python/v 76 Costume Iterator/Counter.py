class Counter:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration


myCounter = Counter(0, 20, 4)

for num in myCounter:
    print(num)

print(type(range(1, 10)))           # <class 'range'>
print(type(iter(range(1, 10))))     # <class 'range_iterator'>

my_counter = Counter(1, 10)
iter(my_counter)
# if we don't implement __iter__(self) => TypeError: 'Counter' object is not iterable
