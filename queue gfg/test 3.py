from queue import Queue

q = Queue()

list_1 = ['1', '2', '3']
# correct:
for i in list_1:
    q.put(i)
print(list(q.queue))

print('1' in q)
