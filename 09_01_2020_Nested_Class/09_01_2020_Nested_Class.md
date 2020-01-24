## Nested class and its use
- A nested or inner class is contained within another class. This could be for reasons of encapsulation, where the inner class is not useful by itself.
- Here is an example of how the classes are laid out.

```sh
class A:
    class B:
        pass
    pass
```
- An inner class in python is a distinct entity in that it does not automatically get access to the outer class members in any special way.

- #### Advantages of inner class:
- **Logical grouping of classes:** If a class is useful to only one other class then it is logical to embed it in that class and keep the two together. Nesting such "helper classes" makes their package more streamlined.
- **Increased encapsulation:** Consider two top-level classes A and B where B needs access to members of A that would otherwise be declared private. By hiding class B within class A A's members can be declared private and B can access them. In addition B itself can be hidden from the outside world.
- **More readable, maintainable code:** Nesting small classes within top-level classes places the code closer to where it is used.

## Use of self keyword
- The self is used to represent the instance of the class.
- With this keyword, you can access the attributes and methods of the class in python.
- It binds the attributes with the given arguments.

##### Example:
```sh
class food():
 
# init method or constructor
def __init__(self, fruit, color):
self.fruit = fruit
self.color = color
 
def show(self):
print("fruit is", self.fruit)
print("color is", self.color )
 
apple = food("apple", "red")
grapes = food("grapes", "green")
 
apple.show()
grapes.show()
```
##### Output:
```sh
Fruit is apple
color is red
Fruit is grapes
color is green
```
- Self is a parameter in function and the user can use a different parameter name in place of it. Although it is advisable to use self because it increases the readability of code.

## Object creation
- The procedure to create an object is similar to a function call.
-  **ob = MyClass()**
- This will create a new instance object named ob. We can access attributes of objects using the object name prefix.
- Attributes may be data or method. Method of an object are corresponding functions of that class.
- Any function object that is a class attribute defines a method for objects of that class.

##### Example:

```sh
class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()
```

## Constructor and its types
- Class functions that begins with double underscore are called special functions as they have special meaning.
- Of one particular interest is the __init__**()** function. This special function gets called whenever a new object of that class is instantiated.
- This type of function is also called constructors in Object Oriented Programming (OOP). We normally use it to initialize all the variables.

```sh
class Number:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i
```
- The above example shows the default constructorin class number.

##### Deleting Attributes and Objects
- We can even delete the object itself, using the del statement.
- When we do c1 = ComplexNumber(1,3), a new instance object is created in memory and the name c1 binds with it.
- On the command del c1, this binding is removed and the name c1 is deleted from the corresponding namespace.
- The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.
- This automatic destruction of unreferenced objects in Python is also called garbage collection.
![](https://cdn.programiz.com/sites/tutorial2program/files/objectReference.jpg)

## Abstraction in Python
- An abstract class can be considered as a blueprint for other classes, allows you to create a set of methods that must be created within any child classes built from your abstract class.
-  A class which contains one or abstract methods is called an abstract class.
-  An abstract method is a method that has declaration but not has any implementation.
- bstract classes are not able to instantiated and it needs subclasses to provide implementations for those abstract methods which are defined in abstract classes.

##### Below code is a simple example of program providing abstraction

```sh
# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 
class Animal(ABC): 

	def move(self): 
		pass

class Human(Animal): 

	def move(self): 
		print("I can walk and run") 

class Snake(Animal): 

	def move(self): 
		print("I can crawl") 

class Dog(Animal): 

	def move(self): 
		print("I can bark") 

class Lion(Animal): 

	def move(self): 
		print("I can roar") 
		
# Driver code 
R = Human() 
R.move() 

K = Snake() 
K.move() 

R = Dog() 
R.move() 

K = Lion() 
K.move() 
```

##### Output:

```sh
I can walk and run
I can crawl
I can bark
I can roar
```

## Polymorphism and its types
- The word polymorphism means having many forms. In programming, polymorphism means same function name (but different signatures) being uses for different types.

##### Example:

```sh
# A simple Python function to demonstrate 
# Polymorphism 

def add(x, y, z = 0): 
	return x + y+z 

# Driver code 
print(add(2, 3)) 
print(add(2, 3, 4)) 
```

##### Output:

```sh
5
9
```

## Inheritance for reusability and its types
- Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

##### Example:

```sh
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```
##### Output:

```sh
John Doe
```
- Depending upon the number of child and parent classes involved, there are four types of inheritance in python.
![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/07/inheritance.png)


## Reference
### Nested class and its use
- https://www.novixys.com/blog/nested-inner-classes-python/
- https://www.edureka.co/community/37598/what-is-the-purpose-of-inner-class-in-python

### Use of self keyword
- https://www.edureka.co/blog/self-in-python/

### Object creation
- https://www.programiz.com/python-programming/class

### Constructor and its types
- https://www.programiz.com/python-programming/class

### Polymorphism and its types
- https://www.geeksforgeeks.org/polymorphism-in-python/

### Inheritance for reusability and its types
- https://www.w3schools.com/python/python_inheritance.asp
- https://www.edureka.co/blog/inheritance-in-python/