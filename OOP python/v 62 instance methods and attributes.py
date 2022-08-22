class Calculator:
    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


calc = Calculator()
print(calc.sum(3, 2))
