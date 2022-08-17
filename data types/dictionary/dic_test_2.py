
if __name__ == '__main__':
    thisDict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
    }
    # key : value
    print(thisDict["brand"])
    print(thisDict)
    for _ in thisDict:
        print(_)
    print(type(thisDict))
