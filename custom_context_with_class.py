class FileStream:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.filestream = open(self.path, self.mode)
        return self.filestream
    def __exit__(self, type, value, traceback):
        self.filestream.close()

with FileStream('hello.txt', 'r') as f:
    print(f.read())

print(f.closed)