from queue import Queue

q = Queue()
print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print(list(q.queue))

print("Full: ", q.full())

print("Elements dequeued from the queue")
print(q.get())
print(list(q.queue))
print(q.get())
print(q.get())

print("Empty: ", q.empty())

q.put(1)
print("Empty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())
