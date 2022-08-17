testTextFile = open("./text.txt")  # mode='r' read(default)
print(testTextFile.read())  # print file
print(testTextFile.read())  # print nothing because after first read cursor is at the end
print('end')

testTextFile.close()
