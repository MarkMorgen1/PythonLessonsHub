# @property Decorator

# The most pythonic way to define getters, setters, and deleters is by using the @property decorator. This decorator is syntactic sugar for using the property() function and helps our code look much cleaner. Let’s take a look:

class Box:
 def __init__(self, weight):
   self.__weight = weight

 @property #The first method must be the getter and is identified using @property.
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight # this is the real 'getter' line


 # The decorators for the setter and deleter are defined by the name of the method that @property is used with, in this case @weight.setter, and @weight.deleter.  '__weight' is used as convention with '__' to denote private access to __weight, but there is no change in programming.
 @weight.setter  
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight

 @weight.deleter # All three methods must use the same member name (ex. weight).
 def weight(self):
   del self.__weight

Let’s break this down:

    First, we have renamed all of our methods to simply be weight().
    Then we denoted our getter with a @property. This marks the property to be used as a prefix for decorating the setter and deleter methods.
    Lastly, we use @weight.setter and @weight.deleter to define our setter and deleter methods, respectively.

This is the equivalent of doing:

weight = property(getWeight, setWeight, delWeight,  "Docstring for the 'weight' property")

And thus giving us the same syntactical advantage as before:

box = Box(10)  # define object 'box' in class Box with weight = 10

box.weight = 5 # set weight of 'box' object to 5
box.weight = -7 # will not work because of 'if' in the setter function 

del box.weight # delete weight of 'box'

Wrap up

To summarize, we learned:

    The limitations of using regular setter and getter methods.
    How to use the property() function to create cleaner getters, setters, and deleters.
    The @property decorator is the most “pythonic” way to use the property() function.

When using the decorator, remember three rules:

    All three methods must use the same member name (ex. weight).
    The first method must be the getter and is identified using @property.
    The decorators for the setter and deleter are defined by the name of the method @property is used with.

Keep the @property decorator in mind when approaching any object-oriented program! It will save time and keep code cleaner and more maintainable.