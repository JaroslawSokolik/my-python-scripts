class Fruit():
    def __init__(self, name, clr):  #  parameters
        self.colour = clr  # class attribute and its value as parameter clr
        self.name = name  # class attribute and its value as parameter name
        
    def details(self):  #  method - function inside a class
        
        print("My name is " + self.name + " and the colour is " + self.colour)
        
apple = Fruit("apple", "red" )  # creating instance of the class with arguments - variable apple is an object
info = apple.details()

"""
Init is the place where we initialize all out attributes, the reason why they're there is because init is automatically
executed with every new class instance.


"""