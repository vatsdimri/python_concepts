# with statement start a context.
# when we are using with statement we don't need to close the file
# the with statment closes the file on exit
# We can use the context manager whenever we have to use and then free up some resourses
with open('hello.txt', 'r') as f:
    print(f.read())

print("1. Closed or not", f.closed)


# The above code is equivalent to 
f = open('hello.txt', 'r')
try:
    print(f.read())
finally:
    f.close()

print("2. Closed or not", f.closed)

# As soon as the code gets out of the


