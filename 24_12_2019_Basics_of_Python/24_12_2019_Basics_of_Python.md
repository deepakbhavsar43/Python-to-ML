## Command Line Arguments
- Python 3 supports four different ways of handling command line arguments.
	- **sys** (oldest and relates directly to **libc**)
	- **getopt** (handles both short, and long options, including the evaluation of 
the parameter values.)
	- **argparse**  (derived from the optparse)
	- **docopt**
- The oldest one is the **sys** module.

	### The sys Module
	 - The sys module implements the command line arguments in a simple list 
structure named sys.argv.
	 - Each list element represents a single argument.
	 - The first one -- **sys.argv[0]** -- is the name of the **Python script.**
	 - The other list elements -- **sys.argv[1] **to** sys.argv[n]** -- are the 
command line **arguments** 2 to n. As a delimiter between the arguments, a space is in 
use.
	 - Argument values that contain a space in it have to be quoted, accordingly.
	 #### Example : Determine the name of the Python script and first argument

```sh
# Python code to demonstrate the use of 'sys' module 
# for command line arguments 
import sys 
# command line arguments are stored in the form 
# of list in sys.argv 
argumentList = sys.argv 
print argumentList 
# Print the name of file 
print sys.argv[0] 
# Print the first argument after the name of file 
print sys.argv[1]  
```
**OUTPUT :**

```
['program1.py', 'test', '1']
program1.py
test
```

### The argparse Module
- The argparse module is available starting in Python 3.2, and an enhancement of the 
optparse module that exists up to Python 2.7.
-  argparse allows the verification of fixed and optional arguments with name checking as 
either UNIX or GNU style.
- As a default optional argument, it includes -h, along with its long version --help. 
This argument is accompanied by a default help message describing the argument.

#### Example : Basic usage of the argparse module

```sh
# include standard modules
import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.parse_args()
```
#### Output:

```sh
$ python3 arguments-argparse-basic.py 
$
$ python3 arguments-argparse-basic.py -h
usage: arguments-argparse-basic.py [-h]

optional arguments:
  -h, --help  show this help message and exit
$
$ python3 arguments-argparse-basic.py --verbose
usage: arguments-argparse-basic.py [-h]
arguments-argparse-basic.py: error: unrecognized arguments: --verbose
$
```

- As the next step, we will add a **custom description to the help message**.
- Initializing the parser allows an additional text.
- Example given below stores the description in the text variable, which is explicitly 
given to the argparse class.
#### Example 6: Adding a description to the help message

```sh
# include standard modules
import argparse
# define the program description
text = 'This is a test program. It demonstrates how to use the argparse module with a 
program description.'
# initiate the parser with a description
parser = argparse.ArgumentParser(description = text)
parser.parse_args()
```
#### Output:

```sh
$ python3 arguments-argparse-description.py --help
usage: arguments-argparse-description.py [-h]

This is a test program. It demonstrates how to use the argparse module with a
program description.

optional arguments:
  -h, --help  show this help message and exit
```

- As the final step we will add an optional argument named -V (UNIX style), which has a 
corresponding GNU style argument named **--version**.
- To do so we use the method **add_argument()** that we call with three parameters 
(displayed for --version, only):
	- the name of the parameter: --version
	- the help text for the parameter: help="show program version"
	- action (without additional value): action="store_true"
- The source code for that is displayed in below example.
- Reading the arguments into the variable called **args is done via the parse_args()** 
method from the parser object.
- Note that you submit both the short and the long version in one call.
- Finally, you check if the attributes **args.V** or **args.version** are set and output 
the version message.

#### Example : Defining an optional argument

```sh
# include standard modules
import argparse
# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
# read arguments from the command line
args = parser.parse_args()
# check for --version or -V
if args.version:
    print("this is myprogram version 0.1")
```
#### Output:

```sh
$ python3 arguments-argparse-optional.py -V
this is myprogram version 0.1
$
$ python3 arguments-argparse-optional.py --version
this is myprogram version 0.1
```

- The - -version argument does not require a value to be given on the command line.
- That's why we set the action argument to "store_true".
- In other cases you need an additional value, for example if you specify a certain 
volume, height, or width.
- This is shown in the next example. As a default case, please** note that all the 
arguments are interpreted as strings**.

#### Example : Defining an optional argument with value

```sh
# include standard modules
import argparse
# initiate the parser
parser = argparse.ArgumentParser()
# add long and short argument
parser.add_argument("--width", "-w", help="set output width")
# read arguments from the command line
args = parser.parse_args()
# check for --width
if args.width:
    print("set output width to %s" % args.width)
```

#### Output:
```sh
$ python3 arguments-argparse-optional2.py -w 10
set output width to 10
$
$ python3 arguments-argparse-optional2.py --width 10
set output width to 10
$
$ python3 arguments-argparse-optional2.py -h
usage: arguments-argparse-optional2.py [-h] [--width WIDTH]

optional arguments:
  -h, --help            show this help message and exit
  --width WIDTH, -w WIDTH
                        set output width
```

- **sys** is fully flexible whereas both **getoptand**, **argparse** require some 
structure.
- In contrast, they cover most of the complex work that sys leaves to your hands.

## Input-Output in Python
- unctions like **input()** and **print()** are widely used for standard input and output 
operations respectively.

#### Output in Python using print() function
- We use the **print()** function to output data to the standard output device (screen).

```sh
print('This sentence is output to the screen')
# Output: This sentence is output to the screen
a = 5
print('The value of a is', a)
# Output: The value of a is 5
```
- In the second print() statement, we can notice that a space was added between the 
string and the value of variable a.
- This is by default, but we can change it.
- The actual syntax of the print() function is
	```print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)```
Here, objects is the value(s) to be printed.
	- The sep separator is used between the values. It defaults into a space 
character.
	- After all values are printed, end is printed. It defaults into a new line.
	- The file is the object where the values are printed and its default value is 
sys.stdout (screen). Here are an example to illustrate this.

```sh
print(1,2,3,4)
# Output: 1 2 3 4
print(1,2,3,4,sep='*')
#Output: 1*2*3*4
print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&
```

#### Input in python
- To allow flexibility we might want to take the input from the user.
- In Python, we have the **input()** function to allow this. The syntax for input() is

```
input([prompt])
```
- where **prompt** is the string we wish to display on the screen. It is optional.

```sh
>>> num = input('Enter a number: ')
Enter a number: 10
>>> num
'10'
```
- Here, we can see that the entered value 10 is a string, not a number. To convert this 
into a number we can use int() or float() functions.

```sh
>>> int('10')
10
>>> float('10')
10.0
```
## Variables in Python
- A variable is a named location used to store data in the memory.

```sh
number = 10
```

#### Example 3: Assigning multiple values to multiple variables

```sh
a, b, c = 5, 3.2, "Hello"
print (a)
print (type(a))

print (b)
print (type(b))

print (c)
print (type(c))
```

##### Output :

```sh
5
<class 'int'>
3.2
<class 'float'>
Hello
<class 'str'>
```

### Constants
- A constant is a type of variable whose value cannot be changed.
- It is helpful to think of constants as containers that hold information which cannot be 
changed later.

Assigning value to a constant in Python
- constants are usually declared and assigned on a module.
- Here, the module means a new file containing variables, functions etc which is imported 
to main file.
- Inside the module, constants are written in **all capital letters** and underscores 
separating the words.

####Example : Declaring and assigning value to a constant
Create a constant.py
```sh
PI = 3.14
GRAVITY = 9.8
```
Create a main.py
```sh
import constant
print(constant.PI)
print(constant.GRAVITY)
```
When you run the program, the output will be:
```sh
3.14
9.8
```

### Literals
- Literal is a raw data given in a variable or constant. In Python, there are various 
types of literals they are as follows:

	- Numeric Literals
		- Numeric Literals are **immutable** (unchangeable).
		- Numeric literals can belong to 3 different numerical types Integer, 
Float, and Complex.

	#### Example : How to use Numeric literals in Python?

```sh
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
```
##### Output:
```sh
10 100 200 300
10.5 150.0
3.14j 3.14 0.0
```
#### String literals
- A string literal is a sequence of characters surrounded by quotes.
- We can use both **single**, **double** or **triple quotes** for a string. And, a 
character literal is a single character surrounded by single or double quotes.
#### Example 7: How to use string literals in Python?

```sh
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
```
#### Boolean literals
- A Boolean literal can have any of the two values: **True** or **False**.

#### Example : How to use boolean literals in Python?

```sh
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
```

#### Special literals
- Python contains one special literal i.e. **None**. We use it to specify to that field 
that is not created.

#### Example : How to use special literals in Python?

```sh
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)
```

#### Literal Collections
- There are four different literal collections List literals, Tuple literals, Dict 
literals, and Set literals.

```sh
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)
```

### Object Identity
- In Python, every object that is created is given a number that uniquely identifies it.
- It is guaranteed that no two objects will have the same identifier during any period in which their lifetimes overlap
- The built-in Python function **id()** returns an object’s integer identifier.

##### Example :

```sh
m = 30
print(id(m))
n =30
print(id(n))
```

##### Output :

```sh
1820157488
1820157488
```

## Operators
### Arithmetic operators in Python
- Arithmetic operators are used with numeric values to perform common mathematical 
operations:

![Arthmetic operators in Python](https://tinyurl.com/rm3owoa)

### Bitwise operators in Python
- Bitwise operators are used to compare (binary) numbers:

![](https://tinyurl.com/rfhffyk)

```sh
# Examples of Bitwise operators 
a = 10
b = 4
# Print bitwise AND operation 
print(a & b) 
# Print bitwise OR operation 
print(a | b) 
# Print bitwise NOT operation 
print(~a) 
# print bitwise XOR operation 
print(a ^ b) 
# print bitwise right shift operation 
print(a >> 2) 
# print bitwise left shift operation 
print(a << 2) 
```
##### Output:

```sh
0
14
-11
14
2
40
```

### Comparison operators in Python (Relational Operators)
-  compares the values. It either returns True or False according to the condition.
![](https://www.engineeringbigdata.com/wp-content/uploads/python-comparison-operators.jpg)
```sh
# Examples of Relational Operators 
a = 13
b = 33
# a > b is False 
print(a > b) 
# a < b is True 
print(a < b) 
# a == b is False 
print(a == b) 
# a != b is True 
print(a != b) 
# a >= b is False 
print(a >= b) 
# a <= b is True 
print(a <= b) 
```
##### Output:
```sh
False
True
False
True
False
True
```
### Assignment operators
- Assignment operators are used to assign values to the variables.

![](https://i1.wp.com/makemeanalyst.com/wp-content/uploads/2017/06/Assignment-Operator.png?resize=590%2C426)

### Operators Precedence and associativity
![](https://media.geeksforgeeks.org/wp-content/uploads/20190708173715/Operator-Precedence-and-Associativity-2.jpg)

## Numbers in Python
- There are three numeric types in Python:
	- **int**
	- **float**
	- **complex**

- Variables of numeric types are created when you assign a value to them:
####Example
```sh
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

## Reference Links
#### Command Line Arguments in Python
- https://stackabuse.com/command-line-arguments-in-python/
- https://docs.python.org/2/howto/argparse.html

#### Input-Output in Python
- https://www.programiz.com/python-programming/input-output-import
- https://www.hackerearth.com/practice/python/getting-started/input-and-output/tutorial/

#### Variables in Python
- https://www.programiz.com/python-programming/variables-constants-literals
- https://www.w3schools.com/python/python_variables.asp
- https://realpython.com/python-variables/#object-identity

#### Operators in Python
- https://www.geeksforgeeks.org/basic-operators-python/
- https://www.w3schools.com/python/python_lists.asp
- https://www.geeksforgeeks.org/basic-operators-python/
- https://www.geeksforgeeks.org/operator-precedence-and-associativity-in-c/
- https://www.programiz.com/python-programming/operators
- https://www.concretepage.com/python/python-bitwise-operators

#### Numbers in Python
- https://www.w3schools.com/python/python_numbers.asp
