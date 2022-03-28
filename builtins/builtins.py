"""abs()
A negative value absolute is that value is positive
"""

print(abs(-7))

"""all()
Function takes a container as an argument.
This Built in Functions returns True if all values in a python iterable have
a Boolean value of True
"""

print(all({'*', '', ''}))

"""any()
Like all(), it takes one argument and returns True if, even one value
in the iterable has a Boolean value of True
"""

print(any((1, 0, 0)))

"""
ascii()
# Returns a printable representation of a python object
# (like a string or a Python list)
"""

print(ascii('ș'))

"""
bin()
Converts an integer to a binary string
"""

print(bin(7))

"""bool()
Converts a value to Boolean
"""

print(bool(1))

"""bytes()
Returns an immutable bytes object
"""

print(bytes(5))

"""bytearray()
Returns a python array of a given byte size
"""

print(bytearray(4))

"""callable()
Tells us if an object can be called.
"""

print(callable(list))
print(callable([1, 2, 3, 4]))

"""chr()
Returns the character in python for an ASCII value
"""

print(chr(48))

"""classmethod()
Returns a class method for a given method.
"""


class fruit:

    def sayhi(self):
        print("Hi, I'm a fruit")


fruit.sayhi = classmethod(fruit.sayhi)
fruit.sayhi

"""compile()
Returns a Python code object. We use it to convert a string code into object
code
"""

exec(compile('a=5\nb=7\nprint(a+b)', '', 'exec'))

"""filter()
Filters out the items for which the condition is True.
"""

print(list(filter(lambda x: x % 2 == 0, [1, 2, 0, False])))

"""float()
It converts an int or a compatible value into a float
"""

print(float(12))

"""format()
Function formats a specified value into a specified format
"""

print(format(0.5, '%'))

"""Frozenset()
Freeze the list, and make it unchangeable
"""

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)

"""getattr()
Function returns the value of the specified attribute from the specified
object
"""


class Person:
    name = "John"
    age = 36
    country = "Norway"


x = getattr(Person, 'age')

print(x)

"""globals()
Function returns the global symbol table as a dictionary.
A symbol table contains necessary information about the current program
"""

x = globals()
print(x)

"""hasattr()
The hasattr() function returns True if the specified object has the specified attribute, otherwise False.
"""

class Person:
    name = "John"
    age = 36
    country = "Norway"

x = hasattr(Person, 'age')

"""hash()
To be completed
"""

"""help()
Executes the built-in help system
"""
# help(print)

"""help()
Converts a number into a hexadecimal value
"""

x = hex(255)
print(x)

"""id()
The id() function returns a unique id for the specified object.
"""

x = ('apple', 'banana', 'cherry')
print(id(x))

"""input()
The input() function allows user input.
"""

print('Enter your name:')
x = input()
print('Hello, ' + x)

"""int()
The int() function converts the specified value into an integer number.
"""

print(int(3.5))

"""isinstance()
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
"""

x = isinstance(5, int)
print(x)

"""issubclass()
The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.
"""
# To be done

"""iter()
Create an iterator object, and print the items
"""

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

"""len()
Return the number of items in a list
"""

print(len("string"))
x = [1, 2, 3]
print(len(x))

"""list()
Function creates a list object.
A list object is a collection which is ordered and changeable.
"""

x = list(('apple', 'banana', 'cherry'))
print(x)

"""locals()
Function returns the local symbol table as a dictionary.
A symbol table contains necessary information about the current program
"""

x = locals()
print(x)

"""map()
"""

# To be completed

"""max()
Return the largest number"""

x = [1, 3 ,6, 1234, 45666]
print(max(x))

"""memoryview()
Create and print a memoryview object
"""
print(memoryview(b"Hello"))

"""min()
Returns the smallest item in an iterable
"""

x = [1, 3 ,6, 1234, 45666]
print(min(x))

