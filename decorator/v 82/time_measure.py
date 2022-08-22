from time import time

startTime = time()
sum([num for num in range(100000000)])
endTime = time()

print(endTime - startTime)
