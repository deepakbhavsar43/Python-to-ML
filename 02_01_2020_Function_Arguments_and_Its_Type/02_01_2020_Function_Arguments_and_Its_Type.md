## Function arguments and its types
- There are various types of Python arguments functions. Let’s learn them one by one:
	- **Default Argument in Python**
	- **Python Keyword Arguments**
	- **Python Arbitrary Arguments**
	- **Conclusion: Python Function Arguments**

## Required function / Position argument
- Required arguments are the arguments passed to a function in correct positional order.
- Here, the number of arguments in the function call should match exactly with the function definition.
- To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows −

```sh
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme()
```
##### Output :

```sh
Traceback (most recent call last):
   File "test.py", line 11, in <module>
      printme();
TypeError: printme() takes exactly 1 argument (0 given)
```

## Keyword arguments of function
- Keyword arguments are related to the function calls.
- When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.

```sh
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;
# Now you can call printme function
printme( str = "My string")
```

##### Output :
```sh
My string
```

## Default function arguments
- A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

```sh
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;
# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )
```

##### Output :
```sh
Name:  miki
Age  50
Name:  miki
Age  35
```

## Variable number of argument of function
- You may need to process a function for more arguments than you specified while defining the function.
- These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.
- An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments.

```sh
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;
# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
```
##### Output :

```sh
Output is:
10
Output is:
70
60
50
```

## Recursive function approach
- Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body.
- Usually, it is returning the return value of this function call.
- If a function definition fulfils the condition of recursion, we call this function a recursive function.
- **Example :**

```sh
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

## Reference Links
- https://data-flair.training/blogs/python-function-arguments/
- https://www.tutorialspoint.com/python/python_functions.htm
https://www.python-course.eu/recursive_functions.php