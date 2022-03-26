# abs()
# A negative value’s absolute is that value is positive

print(abs(-7))

# all()
# Function takes a container as an argument.
# This Built in Functions returns True if all values in a python iterable have
# a Boolean value of True

print(all({'*', '', ''}))

# any()
# Like all(), it takes one argument and returns True if, even one value
# in the iterable has a Boolean value of True

print(any((1, 0, 0)))

# ascii()
# Returns a printable representation of a python object
# (like a string or a Python list)

print(ascii('ș'))

# bin()
# Converts an integer to a binary string

print(bin(7))

# bool()
# Converts a value to Boolean

print(bool(1))

# bytes()
# Returns an immutable bytes object

print(bytes(5))

# bytearray()
# Returns a python array of a given byte size

print(bytearray(4))

# callable()
# Tells us if an object can be called.

print(callable(list))
print(callable([1, 2, 3, 4]))

# chr()
# Returns the character in python for an ASCII value

print(chr(48))

# classmethod()
# Returns a class method for a given method.

class fruit:
    def sayhi(self):
        print("Hi, I'm a fruit")
fruit.sayhi = classmethod(fruit.sayhi)
fruit.sayhi

# compile()
# Returns a Python code object. We use it to convert a string code into object
# code

exec(compile('a=5\nb=7\nprint(a+b)', '', 'exec'))

# Here, ‘exec’ is the mode.
# The parameter before that is the filename for the file form which the code
# is read.Finally, we execute it using exec()

# filter()
# Filters out the items for which the condition is True.

print(list(filter(lambda x: x % 2 == 0, [1, 2, 0, False])))

# float()
# It converts an int or a compatible value into a float

print(float(12))
