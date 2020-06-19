## Duck Typing in Python
- Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc. 
- where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
- The name Duck Typing comes from the phrase:
>"If it looks like a duck and quacks like a duck, it's a duck”

#####Example:

```sh
# Python program to demonstrate 
# duck typing 

class Specialstring: 
	def __len__(self): 
		return 21

# Driver's code 
if __name__ == "__main__": 

	string = Specialstring() 
	print(len(string)) 
```

## Decorators in Python
- Having the basic knowledge of **Assigning Functions to Variables**, **Defining Functions Inside other Functions**, **Passing Functions as Arguments to other Functions**, **Functions Returning other Functions** prerequisited before learning Decorators in Python. 
- A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
- Decorators are usually called before the definition of a function you want to decorate.
- We do this by defining a wrapper inside an enclosed function. As you can see it very similar to the function inside another function that we created earlier.

##### Example: basic example of decorators

```sh
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
```
- Our decorator function takes a function as an argument, and we shall, therefore, define a function and pass it to our decorator.

```sh
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate()
```

##### Output:

```sh
'HELLO THERE'
```

## Practical use of Decorators
- Decorators can be used to calculate the time required for a function to execute.
- It is also used to cache the function result so that next time it wont execute the whole function.

## Exception handling
##### What is an Exception?
- An exception is an error that happens during execution of a program. When that error occurs, Python generate an exception that can be handled, which avoids your program to crash.

##### Why use Exceptions?
- Exceptions are convenient in many ways for handling errors and special conditions in a program. When you think that you have a code which can produce an error then you can use exception handling.

##### Raising an Exception?
- You can raise an exception in your own program by using the raise exception statement.
- Raising an exception breaks current code execution and returns the exception back until it is handled.

##### Exception Errors
- Below is some common exceptions errors in Python:

```sh
IOError
If the file cannot be opened.

ImportError
If python cannot find the module

ValueError
Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value

KeyboardInterrupt
Raised when the user hits the interrupt key (normally Control-C or Delete)

EOFError
Raised when one of the built-in functions (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data
```
##### Exception Errors Examples
- Now, when we know what some of the exception errors means, let's see some examples:

```sh
except IOError:
    print('An error occurred trying to read the file.')

except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print ("NO module found")

except EOFError:
    print('Why did you do an EOF on me?')

except KeyboardInterrupt:
    print('You cancelled the operation.')

except:
    print('An error occurred.')
```
- Try to use as few try blocks as possible and try to distinguish the failure conditions by the kinds of exceptions they throw.

##### How does it work?
- The error handling is done through the use of exceptions that are caught in try blocks and handled in except blocks. If an error is encountered, a try block code execution is stopped and transferred down to the except block. 
- In addition to using an except block after the try block, you can also use the
finally block. 
- The code in the finally block will be executed regardless of whether an exception
occurs.

##### Code Example
- Lets write some code to see what happens when you not use error handling in your
program.
- This program will ask the user to input a number between 1 and 10, and then print
the number.

```sh
number = int(raw_input("Enter a number between 1 - 10"))
print ("you entered number", number)
```
- This program works perfectly fun as long as the user enters a number, but what
happens if the user puts in something else (like a string)?

```sh
Enter a number between 1 - 10
hello
```
- You can see that the program throws us an error when we enter a string.

```sh
Traceback (most recent call last):
  File "enter_number.py", line 1, in 
    number = int(raw_input("Enter a number between 1 - 10 "))
ValueError: invalid literal for int() with base 10: 'hello'
```

- ValueError is an exception type. Let's see how we can use exception handling to
fix the previous program

```sh
import sys

print "Lets fix the previous code with exception handling"

try:
    number = int(raw_input("Enter a number between 1 - 10 "))

except ValueError:
    print "Err.. numbers only"
    sys.exit()

print "you entered number ", number
```
- If we now run the program, and enter a string (instead of a number), we can see
that we get a different output.

```sh
Lets fix the previous code with exception handling
Enter a number between 1 - 10
hello
Err.. numbers only
```

## Referenc links
### Duck Typing in Python
- https://www.geeksforgeeks.org/duck-typing-in-python/

### Decorators in Python
- https://www.datacamp.com/community/tutorials/decorators-python
- https://www.youtube.com/watch?v=mZ5IwFfqvz8
- https://www.youtube.com/watch?v=MjHpMCIvwsY

### Practical use of Decorators

### Exception handling
- https://www.pythonforbeginners.com/error-handling/exception-handling-in-python