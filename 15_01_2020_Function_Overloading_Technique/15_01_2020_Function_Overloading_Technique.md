## Function Overloading technique
![](https://pythonspot.com/wp-content/uploads/2016/03/method-overloading-300x166.png.webp)
- In Python you can define a method in such a way that there are multiple ways to call it. Given a single method or function, we can specify the number of parameters ourself.
- Depending on the function definition, it can be called with zero, one, two or more parameters.
- This is known as method overloading. Not all programming languages support method overloading, but Python does.

##### Method overloading example
- We create a class with one method sayHello().
- The first parameter of this method is set to None, this gives us the option to call it with or without a parameter.
- An object is created based on the class, and we call its method using zero and one parameter.

```sh
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Human()
# Call the method
obj.sayHello()
# Call the method with a parameter
obj.sayHello('Guido')
```
##### Output :

```sh
Hello
Hello Guido
```
- To clarify method overloading, we can now call the method sayHello() in two ways:

```sh
obj.sayHello()
obj.sayHello('Guido')
```