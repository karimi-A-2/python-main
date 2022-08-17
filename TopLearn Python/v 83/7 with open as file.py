# this way don't need to close file it will do it automatically in with scope
with open("./text.txt") as File:
    print(File.read())
    File.seek(0)
    print(File.read())
