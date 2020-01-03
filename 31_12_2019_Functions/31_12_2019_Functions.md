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
- we simply create a function inside another function using the Python's def keyword. Here is an example:

```sh
def function1(): # outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1()
```
## Returning multiple values from function
## User Defined Functions

## Reference Links
### Function and Function calling techniques
- https://www.programiz.com/python-programming/function#return

### Recursive function approach
- https://www.programiz.com/python-programming/recursion

### Inner function and its calling techniques
- https://stackabuse.com/python-nested-functions/

### Returning multiple values from function
### User Defined Functions