def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "Dont Divide By Zero Please !!!"
    except TypeError as error:
        print(error)
        return "first and second must be numbers !!!"


print(divide(1, 'skjdf'))
print(divide(1, 0))
