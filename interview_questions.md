# Interview Questions and Answers

## Conceptual Questions
1. What are python datatypes?  
datatypes are the types of data availabe in the python
for example, integers, strings, float, complex, boolean
    lists, dictionaries, tuples, sets, frozensets, byte, bytearray

2. Explain the difference between mutable and immutable datatypes?  
Mutable datatypes, the individual values of the data can be changed after the creation, but in immutable datatypes once defined we can not change the value

3. Difference between list and tuple?  
List are mutable and tuples are immutables
4. Control flow statements?
if, loop
5. *args and **kwargs in python?
These are used to make python function more flexible. Since by using these we can pass variable number of arguments.
with args we can pass any number of positional arguments. inside the function they can be accessed using args which becomes a list  
with kwargs we can pass key-value pair arguments. Inside the function those can be accessed using the dictionary kwargs 

6. Python built-in data structures?
Lists, dictionaries, tuples, sets etc. Python also provide additional datastructures in the collection modules, like dqueue etc

7. Explain the difference between shallow and deep copy?
    **Shallow copy**shallow copy creates a new object but does not copy the nested objects. It copies the references to the nested objects. If we change the values of the nested object the the changes will be reflected in both the original and the shallow copy
    ```python
    import copy
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original) # shallow copy

    deep = copy.deepcopy(original) # deep copy

    ```
    the deep copy create a seperate object and also copies all the nested objects inside the object.
    The simple "=" operator doesn't create a new object. It only create a new reference to the old object

8. How to handle exception in python?
Using 
```python
try:
    ...
except Exception as e: # we can also write any specific type of exception eg. ValueError, ZeroDivisionError etc
    ...

```
We use `try:` to wrap the code that might raise an exception and use `except:` block to handle specific exception  
We can handle multiple exception by using multiple `except` statements or specifying them as tuple in `except` statement  
We can catch all the exception with `except Exception as e:` line   
We can use `else` block if no exception is raise in the the above code   
Using `finally`, we can use this if we want to run a piece of code regardless of if the exception is raised or not. 
We can raise exception by using `raise` to raise exception manually

```python
try:
    age = -1
    if age<0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)

```

We can also create custom exceptions by subclassing `Exception` class. After that we can raise it using `raise` keyword
```python
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(e)

```

9. What is the difference between `is` and `==` ?
`is` compare identity, ie. if the two objects are the same object in the memory.  whereas `==` compare the value.
we can customize the `==` operator using `__eq__` magic method.

10. How memory management happens in python?
    * Reference counting: counts how many time an object has been referenced in a code
    * Garbage collection: when reference counter for an object goes to zero, garbage collector deletes the object
We can check the reference counting using `sys` module in python
```python
import sys

a = 50.45
b = a
print(sys.getrefcount(a))
```
**interning** is also an important concept. For immutable objects like small integers and short strings to save memory the python interpreter reuses the same object. 

11. Python module?
single python file that can be imported for reusing

12. what are python decorators?






