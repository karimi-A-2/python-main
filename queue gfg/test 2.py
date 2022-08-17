from queue import Queue

q = Queue()

list_1 = ['1', '2', '3']
# correct:
for i in list_1:
    q.put(i)
print(list(q.queue))

list_2 = ['4', '5']
for i in list_2:
    q.put(i)
print(list(q.queue))

# wrong:
# q.put(my_list)
# q.put(i for i in my_list)
# q.put(i) for i in my_list
