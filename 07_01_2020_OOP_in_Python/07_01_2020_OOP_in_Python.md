## Object Oriented programming in Python
- Python is a multi-paradigm programming language. Meaning, it supports different programming approach.
- One of the popular approach to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).
- An object has two characteristics:
	- attributes
	- behavior
- **Lets take an example:**
- Parrot is an object,
	- name, age, color are attributes
	- singing, dancing are behavior
- The concept of OOP in Python focuses on creating reusable code. This concept is also known as **DRY** (Dont Repeat Yourself).
- In Python, the concept of OOP follows some basic principles:

|||
|-|-|
| Inheritance | A process of using details from a new class without modifying existing class. |
| Encapsulation | Hiding the private details of a class from other objects. |
| Polymorphism | A concept of using common operation in different ways for different data input. |

## Concept of Encapsulation using Class
- Using OOP in Python, we can restrict access to methods and variables. This prevent data from direct modification which is called encapsulation.
- In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.
- **Example : Data Encapsulation in Python**

```sh
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
```
##### Output :

```sh
Selling Price: 900
Selling Price: 900
Selling Price: 1000
```
## Characteristics of class and its types
- Class inheritance mechanism
- A derived class that override any method of its base class
- A method can call the method of a base class with the same name
- Python Classes are defined by keyword "class" itself
- Inside classes, you can define functions or methods that are part of the class
- Everything in a class is indented, just like the code in the function, loop, if statement, etc.
- The self argument in Python refers to the object itself. Self is the name preferred by convention by Pythons to indicate the first parameter of instance methods in Python
- Python runtime will pass "self" value automatically when you call an instance method on in instance, whether you provide it deliberately or not
- In Python, a class can inherit attributes and behavior methods from another class called subclass or heir class.