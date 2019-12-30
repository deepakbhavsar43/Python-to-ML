
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

## String in Python

## Dictionaries and its use

## Array and its types

## Manipulate different types of array

## Creation and use of multidimensional array

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
### String in Python
### Dictionaries and its use
### Array and its types
### Manipulate different types of array
### Creation and use of multidimensional array
