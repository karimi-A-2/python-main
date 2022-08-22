def person_get(d, key):
    try:
        return d[key]
    except ValueError:
        return "Value Error"
    except IndexError:
        return "Index Error"


person = {
    'name': 'ali',
    'family': 'karimi'
}

print(person_get(person, 'name'))
print(person_get(person, 'age'))
