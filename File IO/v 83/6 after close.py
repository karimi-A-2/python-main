testTextFile = open("text.txt")  # mode='r' read(default)

textLines = testTextFile.readlines()
print(textLines)

testTextFile.close()

print(testTextFile.read())  # ValueError: I/O operation on closed file.
