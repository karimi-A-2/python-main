# parameters
def sum_to_six(firstNumber):
    return firstNumber + 6


print(sum_to_six(5))
print(sum_to_six(9))


def sum_a_b(firstNumber, secondNumber):
    return firstNumber + secondNumber


print(sum_a_b(19, 6))


def showFullName(firstName, lastName):
    return f"{firstName} {lastName}"


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

myNumbers = [1, 2, 3, 4, 5, 6, 7]  # 16


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers(myNumbers))


def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


print(is_even_number(5))  # false
print(is_even_number(6))  # true
