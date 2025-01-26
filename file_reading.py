# File Reading

file = open("hello.txt", 'w+')
file.write("hello world!")
file.close()
print(file.closed)