## Anonymous / Lambda functions in python
- Python, anonymous function is a function that is defined without a name.
- While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.
- Syntax of Lambda Function in python

```sh
lambda arguments: expression
```
- Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.

- Example of Lambda Function in python

```sh
# Program to show the use of lambda functions
double = lambda x,y,z,a,b: x+y+z+a+b
# Output: 10
print(double(1,1,1,1,1))
```
##### Output :

```sh
C:\Users\deepak.bhavsar\Desktop>python 1.py
5
```

## Filter, Map, Reduce concept in Python
- Lambda functions are used along with built-in functions like** filter()**, **map()** etc.

#### filter()
- The filter() function in Python takes in a function and a list as arguments.
- The function is called with all the items in the list and a new list is returned which contains items for which the function evaluats to True.

#### map()
- The map() function in Python takes in a function and a list.
- The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
- Here is an example use of map() function to double all the items in a list.

#### reduce()
- The reduce() function accepts a function and a sequence and returns a single value calculated as follows:
1. Initially, the function is called with the first two items from the sequence and the result is returned.
2. The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.

- **Syntax:** reduce(function, sequence[, initial]) -> value

- When the initial value is provided, the function is called with the initial value and the first item from the sequence.
- in Python 3, it is moved to functools  module. Therefore to use it, you have to first import it as follows:

```sh
from functools import reduce # only in Python 3
```
- Here is an example which adds all the items in the list.

```sh
>>>
>>> from functools import reduce
>>> 
>>> def do_sum(x1, x2): return x1 + x2
... 
>>> 
>>> reduce(do_sum, [1, 2, 3, 4])
10
>>>
```
