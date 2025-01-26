'''
The decorator takes a function as an argument and wrap the function inside another wrapper function
Using this we can add some features to already defined function
Decorator returns the wropper function
'''

def decorator(func):
    def wrapper():
        print("Before the execution of function")
        func()
        print("After the execution of function")
    return wrapper


#======================== Method 1
# 1. first we define the function
def hello():
    print("Hello, world!")

# 2. first we pass the function into the decorator and return the wrapper function
hello = decorator(hello)
# 3. then we can call the wrapper function
hello()

#======================== Method 2
# 1. We use the decorator right at the top of the function definition with @ symbol
@decorator 
def good_bye():
    print("Good bye!")
# the above lines of code are equivalent to step 1 and step 2 in the first method

# 2. After that we can call the function directly

good_bye()



