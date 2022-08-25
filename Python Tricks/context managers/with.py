with open('hello.txt', 'w') as f:
    f.write('hello, world!')

f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

f = open('hello.txt', 'w')
f.write('hello, world')
f.close()

# Harmful:
# some_lock = threading.Lock()
# some_lock.acquire()
# try:
#     pass  # Do something...
# finally:
#     some_lock.release()
 
# Better:
# with some_lock:
#     pass  # Do something...
