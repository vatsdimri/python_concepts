# creating a custom context manager using the standard python library

from contextlib import contextmanager

# we just use contextmanager decorator
@contextmanager
def filestream(path, mode):
    file = open(path, mode)
    yield file
    file.close()

with filestream('hello.txt', 'r') as f:
    print(f.read())

print(f.closed)