testTextFile = open("./text.txt")  # mode='r' read(default)

textLines = testTextFile.readlines()
print(textLines)

testTextFile.close()
