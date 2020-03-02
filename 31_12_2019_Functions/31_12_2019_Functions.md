## Function and Function calling techniques
### Function
- In Python, function is a group of related statements that perform a specific task.
- Functions help break our program into smaller and modular chunks.
- As our program grows larger and larger, functions make it more organized and manageable.
- It avoids repetition and makes code reusable.
![](https://cdn.programiz.com/sites/tutorial2program/files/python-how-function-works_1.jpg)
- **Syntax of Function**

```sh
def function_name(parameters):
	"""docstring"""
	statement(s)
```
- Above shown is a function definition which consists of following components.
	1. Keyword def marks the start of function header.
	2. A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
	3. Parameters (arguments) through which we pass values to a function. They are optional.
	4. A colon (:) to mark the end of function header.
	5. Optional documentation string (docstring) to describe what the function does.
	6. One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
	7. An optional return statement to return a value from the function.

- **Example of a function**

```sh
def greet(name):
	"""This function greets to
	the person passed in as
	parameter"""
	print("Hello, " + name + ". Good morning!")
```

### Function calling techniques
- Once we have defined a function, we can call it from another function, program or even the Python prompt.
- To call a function we simply type the function name with appropriate parameters.

```sh
>>> greet('Paul')
Hello, Paul. Good morning!
```
## Recursive function approach
- Recursion is the process of defining something in terms of itself.
- The function which calls itself are termed as recursive functions.
- **Example of recursive function**

```sh
# An example of a recursive function to
# find the factorial of a number
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
num = 4
print("The factorial of", num, "is", calc_factorial(num))
```
- **Advantages of Recursion**
- Recursive functions make the code look clean and elegant.
- A complex task can be broken down into simpler sub-problems using recursion.
- Sequence generation is easier with recursion than using some nested iteration.


- **Disadvantages of Recursion**
- Sometimes the logic behind recursion is hard to follow through.
- Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
- Recursive functions are hard to debug.

## Inner function and its calling techniques
- we simply create a function inside another function using the Python's **def** keyword. Here is an example:

```sh
def function1(): # outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()
function1()
```
##### Output :

```sh
Hello from outer function
Hello from inner function
```

- In the above example, function2() has been defined inside function1(), making it an inner function.
- To call function2(), we must first call function1().
- The function1() will then go ahead and call function2() as it has been defined inside it.

## Returning multiple values from function
- It is possible to return multiple values from a function in the form of tuple, list, dictionary or an object of a user defined class

- **Return as tuple**

```sh
>>> def function():
      a=10; b=10
      return a,b

>>> x=function()
>>> type(x)
<class 'tuple'>
>>> x
(10, 10)
>>> x,y=function()
>>> x,y
(10, 10)
```

- **Return as object of user defined class**

```sh
>>> class tmp:
def __init__(self, a,b):
self.a=a
self.b=b


>>> def function():
      a=10; b=10
      t=tmp(a,b)
      return t

>>> x=function()
>>> type(x)
<class '__main__.tmp'>
>>> x.a
10
>>> x.b
10
```

## User Defined Functions
- Python, a user-defined function's declaration begins with the keyword def and followed by the function name.
The function may take arguments(s) as input within the opening and closing parentheses, just after the function name followed by a colon.
After defining the function name and arguments(s) a block of program statement(s) start at the next line and these statement(s) must be indented.
- **Example:**

```sh
def avg_number(x, y):
    print("Average of ",x," and ",y, " is ",(x+y)/2)
avg_number(3, 4)
```

## Reference Links
### Function and Function calling techniques
- https://www.programiz.com/python-programming/function#return

### Recursive function approach
- https://www.programiz.com/python-programming/recursion

### Inner function and its calling techniques
- https://stackabuse.com/python-nested-functions/

### Returning multiple values from function
- https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/

### User Defined Functions
- https://www.w3resource.com/python/python-user-defined-functions.php