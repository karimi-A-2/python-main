testTextFile = open("text.txt")  # mode='r' read(default)
print(testTextFile.read())

testTextFile.seek(1)
print(testTextFile.read())

testTextFile.close()
