# mode='a'  # append
with open("./text.txt", mode='a') as File:
    File.write('this is edited text\n')

with open("./text.txt", mode='a') as File:
    File.write('this is new test text\n')
