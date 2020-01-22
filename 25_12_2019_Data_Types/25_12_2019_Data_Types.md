## Data types in Python
- Python provides various standard data types that define the storage method on each of them. The data types defined in Python are given below.

1.  [Numbers](https://www.javatpoint.com/python-data-types#numbers)
2.  [String](https://www.javatpoint.com/python-data-types#string)
3.  [List](https://www.javatpoint.com/python-data-types#list)
4.  [Tuple](https://www.javatpoint.com/python-data-types#tuple)
5.  [Dictionary](https://www.javatpoint.com/python-data-types#dictionary)

## List
- List in Python are ordered and have a definite count.
- The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index.
- Each element in the list has its definite place in the list, which allows duplicating of elements in the list, with each element having its own distinct place and credibility.
- **append(value_here)** is used to add element at the end of the list.
- **insert(position, value_here)** is used to add value at a defined position. It takes 2 arguments, position where the value is tobe inserted and value.
- **extend()** method is used to add multiple elements at the same time at the end of the list.
- **Pop()** function can also be used to remove and return an element from the set, but by default it removes only the last element of the set, to remove element from a specific position of the List, index of the element is passed as an argument to the pop() method.
- To print a specific range of elements from the list, we use **Slice operation**.


![](https://media.geeksforgeeks.org/wp-content/uploads/List-Slicing.jpg)

- 
#### Creating a list with multiple distinct or duplicate elements

```sh
# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)
#adding element to existing list
List.append('Deepak')
print(List)
#adding element at desired position
List.insert(3,3)
print(List)
List.extend(['Arun','Bhavsar',7])
print(List)
#print the last element of the list (Negative indexing)
print(List[-1])
#remove element from list
List.pop(1)
print(List)
#by default pops last element
List.pop()
print(List)
#slicing method to print specific range from list
print(List[7:10])
```
##### Output

```sh
List with the use of Mixed Values:
[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
[1, 2, 'Geeks', 4, 'For', 6, 'Geeks', 'Deepak']
[1, 2, 'Geeks', 3, 4, 'For', 6, 'Geeks', 'Deepak']
[1, 2, 'Geeks', 3, 4, 'For', 6, 'Geeks', 'Deepak', 'Arun', 'Bhavsar', 7]
7
[1, 'Geeks', 3, 4, 'For', 6, 'Geeks', 'Deepak', 'Arun', 'Bhavsar', 7]
[1, 'Geeks', 3, 4, 'For', 6, 'Geeks', 'Deepak', 'Arun', 'Bhavsar']
['Deepak', 'Arun', 'Bhavsar']
```
## Dynamic input in List
- We often encounter a situation when we need to take number/string as input from user.

```sh
# creating an empty list 
lst = [] 
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
# iterating till the range 
for i in range(0, n): 
	ele = int(input()) 
	lst.append(ele) # adding the element 
	
print(lst) 
```

##### Output:
![](https://media.geeksforgeeks.org/wp-content/uploads/list_input1.png)

## Tuples in Python
- A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
- The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
- A tuple can have any number of items and they may be of different types (**integer**, **float**, **list**, **string**, etc.).
- A tuple can also be created without using parentheses. This is known as tuple packing.
```
my_tuple = 3, 4.6, "dog"
```
- Having one element within parentheses is not enough. We will need a **trailing comm**a to indicate that it is, in fact, a tuple.
- Below code shows some operations with tuple.

```sh
# Empty tuple
my_tuple = ()
print(my_tuple) #output: ()
# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple) #output: (1, 2, 3)
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple) #output: (1, 'Hello', 3.4)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple) #putput: ('mouse', [8, 4, 6], (1, 2, 3))
#tuple without using parenthesis
my_tuple = 1, 2, 3, "Deepak", "Bhavsar"
print(my_tuple) #output: (1, 2, 3, 'Deepak', 'Bhavsar')
a,b,c,d,e = my_tuple
print(a) #output: 1
print(b) #output: 2
print(c) #output: 3
print(d) #output: Deepak
print(e) #output: Bhavsar
#We will need a trailing comma to indicate that it is a tuple. 
my_tuple = "Deepak"
print(type(my_tuple)) #output: <class 'str'>
my_tuple = "Deepak",
print(type(my_tuple)) #output: <class 'tuple'>
#Access specific element using index
my_tuple = "Deepak",[1,2,3],['a','b','c']
print(my_tuple[1]) #output: [1, 2, 3]
print(my_tuple[2][1]) #output: b
#The index of -1 refers to the last item, -2 to the second last item and so on.
print(my_tuple[-1]) #output: ['a', 'b', 'c']
#slicing to access specific range of elements
print(my_tuple[1:3]) #output: ([1, 2, 3], ['a', 'b', 'c'])
#concate two tuples
print(my_tuple + my_tuple) #output: ('Deepak', [1, 2, 3], ['a', 'b', 'c'], 'Deepak', [1, 2, 3], ['a', 'b', 'c'])
#as tuple is immutable value cannot be changed
print('\n') # goes to new line
my_tuple[1] = 'Bhavsar'
```
##### Output:
```sh
C:\Users\deepak.bhavsar\Desktop>python Tuple.py
()
(1, 2, 3)
(1, 'Hello', 3.4)
('mouse', [8, 4, 6], (1, 2, 3))
(1, 2, 3, 'Deepak', 'Bhavsar')
1
2
3
Deepak
Bhavsar
<class 'str'>
<class 'tuple'>
[1, 2, 3]
b
['a', 'b', 'c']
([1, 2, 3], ['a', 'b', 'c'])
('Deepak', [1, 2, 3], ['a', 'b', 'c'], 'Deepak', [1, 2, 3], ['a', 'b', 'c'])


Traceback (most recent call last):
  File "Tuple.py", line 39, in <module>
    my_tuple[1] = 'Bhavsar'
TypeError: 'tuple' object does not support item assignment
```
- #### Code for printing the length of a tuple 

```sh
tuple2 = ('python', 'geek') 
print(len(tuple2)) 
```
#### Output:
```sh
 2
```

## Set in Python
- A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.
- Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
- A set is created by placing all the items (elements) inside curly braces **{}**, separated by comma or by using the built-in function **set()**.

##### Example below shows how to create set
```sh
# set of integers
my_set = {1, 2, 3}
print(my_set)
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
#creating set from list
my_set = set([4, 5, 'Deepak'])
print(my_set)
```

##### Output:
```sh
{1, 2, 3}
{1.0, 'Hello', (1, 2, 3)}
{4, 5, 'Deepak'}
```
- Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements we use the set() function without any argument.

```sh
# initialize a with {}
a = {}
# check data type of a
# Output: <class 'dict'>
print(type(a))
# initialize a with set()
a = set()
# check data type of a
# Output: <class 'set'>
print(type(a))
```
- **How to change a set in Python?**
	- Sets are mutable. But since they are unordered, indexing have no meaning.
	- We cannot access or change an element of set using indexing or slicing. Set does not support it.
	- We can add single element using the **add()** method and multiple elements using the **update()** method.
	- The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

```sh
# initialize my_set
my_set = {1,3}
print(my_set)
# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)
# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)
# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)
```

- ##### How to remove elements from a set?
- A particular item can be removed from set using methods, **discard()** and **remove()**.
- The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.
- The following example will illustrate this.
- We can also remove all items from a set using **clear()**.

```sh
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)
# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)
# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)
# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)
# remove an element
# not present in my_set
# If you uncomment line 27,
# you will get an error.
# Output: KeyError: 2

#my_set.remove(2)
```

##### Output:

```sh
{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
```

#### Python Set Operations
- Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference. We can do this with operators or methods.

Let us consider the following two sets for the following operations.

```sh
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

#### Set Union
![](https://cdn.programiz.com/sites/tutorial2program/files/set-union.jpg)

- Union of A and B is a set of all elements from both sets.
- Union is performed using | operator. Same can be accomplished using the method **union()**.

```sh
	# initialize A and B
	A = {1, 2, 3, 4, 5}
	B = {4, 5, 6, 7, 8}
	# use | operator
	# Output: {1, 2, 3, 4, 5, 6, 7, 8}
	print(A | B)
	c= A.union(B)
	print(c)
```
##### Output:
```sh
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
```

#### Set Intersection
![](https://cdn.programiz.com/sites/tutorial2program/files/set-intersection.jpg)

- Intersection of A and B is a set of elements that are common in both sets.
- Intersection is performed using & operator. Same can be accomplished using the method **intersection()**.

```sh
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use & operator
# Output: {4, 5}
print(A & B)
c = A.intersection(B)
print(c)
```

##### Output:

```sh
{4, 5}
{4, 5}
```

#### Set Difference
![](https://cdn.programiz.com/sites/tutorial2program/files/set-difference.jpg)

- Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly, B - A is a set of element in B but not in A.
- Difference is performed using - operator. Same can be accomplished using the method **difference()**.

```sh
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use - operator on A
# Output: {1, 2, 3}
print(A - B)
c = A.difference(B)
print(c)
```
##### Output:

```sh
{1, 2, 3}
{1, 2, 3}
```
#### Set Symmetric Difference
![](https://cdn.programiz.com/sites/tutorial2program/files/set-symmetric-difference.jpg)

- Symmetric Difference of A and B is a set of elements in both A and B **except those that are common in both**.
- Symmetric difference is performed using **^** operator. Same can be accomplished using the method **symmetric_difference()**.

```sh
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
c = A.symmetric_difference(B)
print(c)
```
##### Output:
```sh
{1, 2, 3, 6, 7, 8}
{1, 2, 3, 6, 7, 8}
```
#### Different Python Set Methods
| Method | Description |
|----------|--------------|
| add() | Adds an element to the set |
| clear() | oves all elements from the set |
| copy() | Returns a copy of the set |
| difference() | Returns the difference of two or more sets as a new set |
| difference_update() | Removes all elements of another set from this set |
| discard() | Removes an element from the set if it is a member. (Do nothing if the element is not in set) |
| intersection() | Returns the intersection of two sets as a new set |
| intersection_update() | Updates the set with the intersection of itself and another |
| isdisjoint() | Returns True if two sets have a null intersection |
| issubset() | Returns True if another set contains this set |
| issuperset() | Returns True if this set contains another set |
| pop() | Removes and returns an arbitary set element. Raise KeyError if the set is empty |
| remove() | Removes an element from the set. If the element is not a member, raise a KeyError |
| symmetric_difference() | Returns the symmetric difference of two sets as a new set |
| symmetric_difference_update() | Updates a set with the symmetric difference of itself and another |
| union() | Returns the union of sets in a new set |
| update() | Updates the set with the union of itself and others |

## Range in python
- Pythons built-in range function is handy when you need to perform an action a specific number of times. 
- **range()** in Python 2 and **range()** in Python 3 may share a name, they are entirely different 
##### The below example 
```sh
x = range(6)
print(type(x))
for n in x:
  print(n)
```
##### Output :
```sh
<class 'range'>
0
1
2
3
4
5
```
#### Range Objects with Float Numbers
- The range function does not work with floats. Only integer values can be specified as the start, stop and step arguments.
```sh
# floats with python range
for i in range(0.1, 0.5, 0.1):
    print(i)
```
##### Output :
```sh
TypeError                                 Traceback (most recent call last)
<ipython-input-13-a83306d87fcd> in <module>
       # floats with python range
       for i in range(0.1, 0.5, 0.1):
           print(i)
TypeError: 'float' object cannot be interpreted as an integer
```
- There are three ways you can call range():
	- range(stop) takes one argument.
	- range(start, stop) takes two arguments.
	- range(start, stop, step) takes three arguments.
	
#### range(stop)
- When you call range() with one argument, you will get a series of numbers that starts at 0 and includes every whole number up to, but not including, the number you have provided as the stop.

```sh
for i in range(3):
    print(i)
```

##### Output :
```sh
0
1
2
```

#### range(start, stop)
- When you call range() with two arguments, you get to decide not only where the series of numbers stops but also where it starts, so you dont have to start at 0 all the time. You can use range() to generate a series of numbers from A to B using a range(A, B). Lets find out how to generate a range starting at 1.

```sh
for i in range(1, 8):
    print(i)
```
##### Output :
```sh
1
2
3
4
5
6
7
```

#### range(start, stop, step)
- When you call range() with three arguments, you can choose not only where the series of numbers will start and stop but also how big the difference will be between one number and the next.
- If you dont provide a step, then range() will automatically behave as if the step is 1.

```sh
for i in range(3, 16, 3):
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")
```

##### Output :

```sh
3 divided by 3 is 1.
6 divided by 3 is 2.
9 divided by 3 is 3.
12 divided by 3 is 4.
15 divided by 3 is 5.
```
#### Access Python range() result with its index value
- **range()** is constructor returns a range object which is nothing but a sequence of numbers, this range object can also be accessed by its index using slice notation.

```sh
print("accessing python range objet with its index")
first_number = range(0,10)[0] #printing 0th position number i.e. index ZERO means first number
print("First number in given range is:  ", first_number)
fifth_number = range(0,10)[4]
print("fifth number in given range is:  ", fifth_number)
```
##### Output :
```sh
accessing python range objet with its index
First number in given range is:   0
fifth number in given range is:   4
```
## String in Python
- A string is a sequence of characters.
- Strings can be created by enclosing characters inside a **single quote** or **double quotes**. Even **triple quotes** can be used in Python but generally used to represent multiline strings and docstrings.

```sh
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
```
##### Output :
```sh
Hello
Hello
Hello
Hello, welcome to
           the world of Python
```

- We **can access individual characters** using indexing and a range of characters using slicing. Index starts from 0.

```sh
str = 'programiz'
print('str = ', str)
#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])
```
##### Output :

```sh
# index must be in range
my_string[15]  
...
IndexError: string index out of range
# index must be an integer
my_string[1.5] 
...
TypeError: string indices must be integers
```
- Slicing can be best visualized by considering the index to be between the elements as shown below.
- If we want to access a range, we need the index that will slice the portion from the string.

![](https://media.geeksforgeeks.org/wp-content/uploads/String-Indexing.jpg)

- Strings are **immutable**. This means that elements of a string cannot be changed once it has been assigned.

```sh
 >>>my_string = 'programiz'
 >>>my_string[5] = 'a'
...
TypeError: 'str' object does not support item assignment
```
### Python String Operations
#### Concatenation of Two or More Strings
- Joining of two or more strings into a single one is called concatenation.
- The + operator does this in Python. Simply writing two string literals together also concatenates them.
- The * operator can be used to repeat the string for a given number of times.

```sh
str1 = 'Hello'
str2 ='World!'
# using +
print('str1 + str2 = ', str1 + str2)
# using *
print('str1 * 3 =', str1 * 3)
```

##### Output :
```sh
str1 + str2 =  HelloWorld!
str1 * 3 = HelloHelloHello
```

#### Iterating through String
- Using for loop we can iterate through a string. Here is an example to count the number of 'a' in a string.

```sh
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
```

##### Output :
```sh
3 letters found
```
#### String Membership Test
- We can test if a sub string exists within a string or not, using the keyword **in**.

```sh
>>> 'a' in 'program'
True
>>> 'at' not in 'battle'
False
```

#### Built-in functions to Work with Python
- Some of the commonly used ones are enumerate() and len().
- The **enumerate()** function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
- Similarly, **len()** returns the length (number of characters) of the string.

```sh
str = 'Deepak'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#character count
print('len(str) = ', len(str))
```

##### Output :

```sh
list(enumerate(str) =  [(0, 'D'), (1, 'e'), (2, 'e'), (3, 'p'), (4, 'a'), (5, 'k')]
len(str) =  6
```
#### Common Python String Methods
- There are numerous methods available with the string object.
- The **format()** method that we mentioned above is one of them. Some of the commonly used methods are **lower()**, **upper()**,** join()**, **split()**, **find()**, **replace()** etc. 

```sh
"PrOgRaMiZ".lower()
#Output : programmiz
"PrOgRaMiZ".upper()
#Output : PROGRAMIZ
"This will split all words into a list".split()
#Output : ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
#Output : 'This will join all words into a string'
'Happy New Year'.find('ew')
#Output : 7
'Happy New Year'.replace('Happy','Brilliant')
#Output : 'Brilliant New Year'
```

## Dictionaries and its use
- Dictionaries are Pythons implementation of a data structure that is more generally known as an associative array.
- A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.
- You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces (**{}**). A colon (**:**) separates each key from its associated value.
- The following defines a dictionary that maps a location to the name of its corresponding Major League Baseball team:

```sh
MLB_team = {
     'Colorado' : 'Rockies',
     'Boston'   : 'Red Sox',
     'Minnesota': 'Twins',
     'Milwaukee': 'Brewers',
     'Seattle'  : 'Mariners'
}
```

![](https://files.realpython.com/media/t.b3e3d8f2d100.png)

- You can also construct a dictionary with the built-in **dict()** function. The argument to dict() should be a sequence of **key-value pairs.** A list of tuples works well for this:

```sh
MLB_team = dict([
     ('Colorado', 'Rockies'),
     ('Boston', 'Red Sox'),
     ('Minnesota', 'Twins'),
     ('Milwaukee', 'Brewers'),
     ('Seattle', 'Mariners')
])
```
#### Nested Dictionary

```sh
# Creating a Nested Dictionary 
# as shown in the below image 
Dict = {1: 'Geeks', 2: 'For', 
		3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
```
![](https://media.geeksforgeeks.org/wp-content/uploads/Dictionary-Creation-1.jpg)

- Dictionary elements are not accessed by numerical index:

```sh
MLB_team[1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    MLB_team[1]
KeyError: 1
```
#### Accessing Dictionary Values

```sh
MLB_team['Minnesota']
'Twins'
MLB_team['Colorado']
'Rockies'
```
- If you refer to a key that is not in the dictionary, Python raises an exception:

```sh
>>>MLB_team['Toronto']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    MLB_team['Toronto']
KeyError: 'Toronto'
```
- Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:

```sh
>>>MLB_team['Kansas City'] = 'Royals'
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners', 'Kansas City': 'Royals'}
```
- If you want to update an entry, you can just assign a new value to an existing key:

```sh
>>> MLB_team['Seattle'] = 'Seahawks'
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Seahawks', 'Kansas City': 'Royals'}
```
- To delete an entry, use the del statement, specifying the key to delete:

```sh
>>> del MLB_team['Seattle']
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}
```

#### Restrictions on Dictionary Keys
- Almost any type of value can be used as a dictionary key in Python. You just saw this example, where integer, float, and Boolean objects are used as keys:

```sh
>>> foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
>>> foo
{42: 'aaa', 2.78: 'bbb', True: 'ccc'}
```
- You can even use built-in objects like types and functions:

```sh
>>> d = {int: 1, float: 2, bool: 3}
>>> d
{<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}
>>> d[float]
2
>>> d = {bin: 1, hex: 2, oct: 3}
>>> d[oct]
3
```

- A tuple can also be a dictionary key, because tuples are immutable:

```sh
>>> d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
>>> d[(1,1)]
'a'
>>> d[(2,1)]
'c'
```
- neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable:

```sh
>>> d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
TypeError: unhashable type: 'list'
```
#### Restrictions on Dictionary Values
- There are no restrictions on dictionary values. Literally none at all. 
- A dictionary value can be any type of object Python supports, including mutable types like lists and dictionaries, and user-defined objects.
- There is also no restriction against a particular value appearing in a dictionary multiple times:

```sh
>>> d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
>>> d
{0: 'a', 1: 'a', 2: 'a', 3: 'a'}
>>> d[0] == d[1] == d[2]
True
```

#### Operators and Built-in Functions
- For example, the **in** and **not** in operators return True or False according to whether the specified operand occurs as a key in the dictionary:

```sh
>>> MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}
>>> 'Milwaukee' in MLB_team
True
>>> 'Toronto' in MLB_team
False
>>> 'Toronto' not in MLB_team
True
```

- The **len()** function returns the number of key-value pairs in a dictionary:

```sh
>>> MLB_team = {
...     'Colorado' : 'Rockies',
...     'Boston'   : 'Red Sox',
...     'Minnesota': 'Twins',
...     'Milwaukee': 'Brewers',
...     'Seattle'  : 'Mariners'
... }
>>> len(MLB_team)
5
```
#### Built-in Dictionary Methods
- There are several built-in methods that can be invoked on dictionaries. In fact, in some cases, the list and dictionary methods share the same name.

- **clear()** empties dictionary d of all key-value pairs:

```sh
>>> d
{'a': 10, 'b': 20, 'c': 30}
>>> d.clear()
>>> d
{}
```
- The Python dictionary **.get()** method provides a convenient way of getting the value of a key from a dictionary without checking ahead of time whether the key exists, and **without raising an error**.
- get(<key>) searches dictionary d for <key> and returns the associated value if it is found. If <key> is not found, it returns None:

```sh
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> print(d.get('b'))
20
>>> print(d.get('z'))
None
```
- If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:

```sh
>>> print(d.get('z', -1))
-1
```

- **items()**  returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the keys value:

```sh
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> list(d.items())
[('a', 10), ('b', 20), ('c', 30)]
>>> list(d.items())[1][0]
'b'
>>> list(d.items())[1][1]
20
```
- **keys()** returns a list of all keys in d:

```sh
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}
>>> list(d.keys())
['a', 'b', 'c']
```

- **values()** returns a list of all values in d:

```sh
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}
>>> list(d.values())
[10, 20, 30]
```

- pop(**key**) removes **key** and returns its associated value and raises an exception if key is not present in dictionary.

```sh
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d.pop('b')
20
>>> d
{'a': 10, 'c': 30}
>>> d.pop('z')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.pop('z')
KeyError: 'z'
```
- **popitem()** removes a random, arbitrary key-value pair from d and returns it as a tuple:

```sh
>>> d.popitem()
('c', 30)
>>> d
{'a': 10, 'b': 20}
>>> d.popitem()
('b', 20)
>>> d
{'a': 10}
>>>d={}
>>>d.popitem()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
```

- **update(obj)** Merges a dictionary with another dictionary or with an iterable of key-value pairs.
- If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:
	- If the key is not present in d, the key-value pair from <obj> is added to d.
	- If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.

Here is an example showing two dictionaries merged together:

```sh
>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d2 = {'b': 200, 'd': 400}
>>> d1.update(d2)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
```

## Array and its types
- Array in Python can be created by importing array module. array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.
-  we need to import array module to create arrays. For example:

```sh
import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
print(a)
```
##### Output :

```sh
array('d', [1.1, 3.5, 4.5])
```
- we created an array of float type. The letter 'd' is a type code. This determines the type of the array during creation.

Commonly used type codes:

![](https://www.askpython.com/wp-content/uploads/2019/09/python-array-supported-type-code-1024x624.png)

- We use indices to **access elements of an array**:

```sh
import array as arr
a = arr.array('i', [2, 4, 6, 8])
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])
```
##### Output :

```sh
C:\Users\deepak.bhavsar\Desktop>python 1.py
First element: 2
Second element: 4
Last element: 8
```
- We can access a range of items in an array by using the slicing operator :

```sh
import array as arr
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end
```

##### Output :
```sh
array('i', [62, 5, 42])
array('i', [2, 5, 62])
array('i', [52, 48, 5])
array('i', [2, 5, 62, 5, 42, 52, 48, 5])
```
- Arrays are mutable; their elements can be changed in a similar way like lists.

```sh
import array as arr
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
# changing first element
numbers[0] = 0    
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])
# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])
```
 - We can add one item to a list using the append() method, or add several items using extend() method.

```sh
 import array as arr
numbers = arr.array('i', [1, 2, 3])
numbers.append(4)
print(numbers)     # Output: array('i', [1, 2, 3, 4])
# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7]) 
print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])
 ```
- We can delete one or more items from an array using Python's del statement.

```sh
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4])
del number[2] # removing third element
print(number) # Output: array('i', [1, 2, 3, 4])
del number # deleting entire array
print(number) # Error: array is not defined
```

- We can use the remove() method to remove the given item, and pop() method to remove an item at the given index.

```sh
import array as arr
numbers = arr.array('i', [10, 11, 12, 12, 13])
numbers.remove(12)
print(numbers)   # Output: array('i', [10, 11, 12, 13])
print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])
```

## Creation and use of multidimensional array
- Two dimensional array is an array within an array. It is an array of arrays.

#### Accessing Values in a Two Dimensional Array
- The data elements in two dimesnional arrays can be accessed using two indices. One index referring to the main or parent array and another index referring to the position of the data element in the inner array.
- If we mention only one index then the entire inner array is printed for that index position. The example below illustrates how it works.

```sh
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0])
print(T[1][2])
```
##### Output :

```sh
[11, 12, 5, 2]
10
```
- To print out the entire two dimensional array we can use python for loop as shown below. We use end of line to print out the values in different rows.

```sh
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
```
##### Output :

```sh
11 12 5 2 
15 6 10 
10 8 12 5 
12 15 8 6 
```
##### Inserting Values in Two Dimensional Array
- We can insert new data elements at specific position by using the insert() method and specifying the index. In the below example a new data element is inserted at index position 2.

```sh
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
    for c in r:
        print(c,end = " ")
    print()
```
##### Output :
```sh
11 12 5 2 
15 6 10 
0 5 11 13 6 
10 8 12 5 
12 15 8 6 
```

##### Updating Values in Two Dimensional Array
- We can update the entire inner array or some specific data elements of the inner array by reassigning the values using the array index.

```sh
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
T[2] = [11,9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c,end = " ")
    print()
```

##### Output :

```sh
11 12 5 7 
15 6 10 
11 9 
12 15 8 6 
```
#### Deleting the Values in Two Dimensional Array
- We can delete the entire inner array or some specific data elements of the inner array by reassigning the values using the **del()** method with index.

```sh
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
del T[3]
for r in T:
    for c in r:
        print(c,end = " ")
    print()
```
##### Output :

```sh
11 12 5 2 
15 6 10 
10 8 12 5 
```

## Some function wich can be used with all DataTypes

### any() function inython
- Python any() function accepts iterable (list, tuple, dictionary etc.) as an argument and return true if any of the element in iterable is true, else it returns false. If iterable is empty then any() method returns false.
- The any() function returns true if any of the element in the passed list is true.

```sh
# all values are true
lis1 = [10, 20, 30, 40]
print(any(lis1))
```

##### Output:

```sh
True
```
### all() function in Python
- If all the elements in the passed iterable are true then all() function returns true else it returns false.
- If the iterable is empty then also this function returns true.
- The all() function can be used on any iterable such as lists, tuples, dictionaries etc.

### accumulate() function in python
- This function makes an iterator that returns the results of a function.
- Functions can be passed around very much like variables. 
- The **accumulate()** function takes a function as an argument. It also takes an **iterable**.
- This **example** uses the max function.

```sh
data = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(data, max)
for each in result:
    print(each)
```

##### Output:
```sh
5
5
6
6
6
9
9
```

## Reference links

### Data types in Python
- [https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp)
- [https://www.javatpoint.com/python-data-types](https://www.javatpoint.com/python-data-types)

### List in Python
- [https://www.geeksforgeeks.org/python-list/](https://www.geeksforgeeks.org/python-list/)

### Dynamic input in List
- [https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/](https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/) 

### Tuples in Python
- [https://realpython.com/python-lists-tuples/](https://realpython.com/python-lists-tuples/)
- [https://www.programiz.com/python-programming/tuple](https://www.programiz.com/python-programming/tuple) 
- https://www.geeksforgeeks.org/tuples-in-python/

### Set in Python
- https://www.programiz.com/python-programming/set
- https://www.geeksforgeeks.org/sets-in-python/

### Range in python
- https://realpython.com/python-range/#the-history-of-pythons-range-function
- https://www.dataquest.io/blog/python-range-tutorial/
- https://pynative.com/python-range-function/

### String in Python
- https://www.programiz.com/python-programming/string
- https://www.programiz.com/python-programming/methods/string (various python string methods)
- https://www.w3schools.com/python/python_strings.asp
- https://www.geeksforgeeks.org/python-strings/

### Dictionaries and its use
- https://www.geeksforgeeks.org/python-dictionary/
- https://www.programiz.com/python-programming/dictionary
- https://www.w3schools.com/python/ref_dictionary_popitem.asp

### Array and its types
- https://www.geeksforgeeks.org/python-arrays/
- https://www.programiz.com/python-programming/array
- https://www.thegeekstuff.com/2013/08/python-array/

### Creation and use of multidimensional array
- https://www.tutorialspoint.com/python_data_structure/python_2darray.htm
- https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

### Some function wich can be used with all DataTypes
- https://beginnersbook.com/2019/03/python-any-function/
- https://beginnersbook.com/2019/03/python-all-function/
- https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8