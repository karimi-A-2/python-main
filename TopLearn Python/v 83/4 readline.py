testTextFile = open("./text.txt")  # mode='r' read(default)

print(testTextFile.readline())  # 'first line\n'
print(testTextFile.readline())  # 'second line\n'
print(testTextFile.readline())  # 'third line'

testTextFile.close()
