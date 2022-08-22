def sayHello():
    print("hello")
    print("-------------")


sayHello()
sayHello()
sayHello()
sayHello()

for i in range(4):
    sayHello()


def print_square_of_7():
    print(7 ** 2)


print_square_of_7()


def square_of_7():
    # commands
    print("I Am Before Return")
    return 7 ** 2
    print("I Am After Return")


print(square_of_7())


def add_numbers():
    a = 4
    b = 7
    return a + b


print(add_numbers())


# parameters
def sum_to_six(firstNumber):
    return firstNumber + 6


print(sum_to_six(5))
print(sum_to_six(9))


def sum_a_b(first, second):
    return first + second


print(sum_a_b(19, 6))


def showFullName(first_name, last_name):
    return f"{first_name} {last_name}"


name = "mohammad"
family = "ordookhani"
print(showFullName(name, family))

person = {
    "name": "mohammad",
    "family": "ordookhani"
}
print(showFullName(person["name"], person["family"]))


def divide(num_1, num_2):
    return num_1 / num_2


print(divide(3, 5))
print(divide(5, 3))


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


myNumbers = [1, 2, 3, 4, 5, 6, 7]  # 16
print(sum_odd_numbers(myNumbers))


def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


print(is_even_number(5))  # false
print(is_even_number(6))  # true
