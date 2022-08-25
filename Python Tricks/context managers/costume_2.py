from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        file = open(name, 'w')
        yield file
    finally:
        file.close()


with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
