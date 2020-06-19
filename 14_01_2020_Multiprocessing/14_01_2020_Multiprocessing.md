## Multiprocessing application development
- There are plenty of classes in python multiprocessing module for building a parallel program. Among them, three basic classes are **Process**, **Queue** and Lock. These classes will help you to build a parallel program.
- To make a parallel program useful, you have to know how many cores are there in you pc. Python Multiprocessing module enables you to know that. The following simple code will print the number of cores in your pc.

```sh
import multiprocessing
print("Number of cpu : ", multiprocessing.cpu_count())
```
- Let us consider a simple example using multiprocessing module:

```sh
# importing the multiprocessing module 
import multiprocessing 

def print_cube(num): 
	""" 
	function to print cube of given num 
	"""
	print("Cube: {}".format(num * num * num)) 

def print_square(num): 
	""" 
	function to print square of given num 
	"""
	print("Square: {}".format(num * num)) 

if __name__ == "__main__": 
	# creating processes 
	p1 = multiprocessing.Process(target=print_square, args=(10, )) 
	p2 = multiprocessing.Process(target=print_cube, args=(10, )) 

	# starting process 1 
	p1.start() 
	# starting process 2 
	p2.start() 

	# wait until process 1 is finished 
	p1.join() 
	# wait until process 2 is finished 
	p2.join() 

	# both processes finished 
	print("Done!") 
```

##### Output:

```sh
Square: 100
Cube: 1000
Done!
```

- ##### Let us try to understand the above code:
- To import the multiprocessing module, we do:
		import multiprocessing
- To create a process, we create an object of Process class. It takes following arguments:
	- **target**: the function to be executed by process
	- **args**: the arguments to be passed to the target function
Note: **Process** constructor takes many other arguments also which will be discussed later. In above example, we created 2 processes with different target functions:
```sh
p1 = multiprocessing.Process(target=print_square, args=(10, ))
p2 = multiprocessing.Process(target=print_cube, args=(10, ))
```
- To start a process, we use start method of Process class.
```sh
p1.start()
p2.start()
```
- Once the processes start, the current program also keeps on executing. In order to stop execution of current program until a process is complete, we use join method.
```sh
p1.join()
p2.join()
```
- As a result, the current program will first wait for the completion of p1 and then p2. Once, they are completed, the next statements of current program are executed.

## Multitasking using thread
- A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).
- a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process!
- A thread contains all this information in a Thread Control Block (TCB):
	- **Thread Identifier**: Unique id (TID) is assigned to every new thread
	- **Stack pointer**: Points to thread’s stack in the process. Stack contains the local variables under threads scope.
	- **Program counter**: a register which stores the address of the instruction currently being executed by thread.
	- **Thread state**: can be running, ready, waiting, start or done.
	- **Threads register set**: registers assigned to thread for computations.
	- **Parent process Pointer**: A pointer to the Process control block (PCB) of the process that the thread lives on.
- Multiple threads can exist within one process where:
	- Each thread contains its own **register set** and **local variables** **(stored in stack)**.
	- All thread of a process share **global variables** **(stored in heap)** and the **program code**.
- Consider the diagram below to understand how multiple threads exist in memory:
![](https://media.geeksforgeeks.org/wp-content/uploads/multithreading-python-21.png)
- Considering the example given above to calculate square and cube

## Thread Synchronisation techniques
- Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section.
>Critical section refers to the parts of the program where the shared resource is accessed.

- For example, in the diagram below, 3 threads try to access shared resource or critical section at the same time.
![](https://media.geeksforgeeks.org/wp-content/uploads/multithreading-python-1.png)

- Concurrent accesses to shared resource can lead to race condition.

## Single threaded vs multithread application development
- Single threaded processes contain the execution of instructions in a single sequence.
- The opposite of single threaded processes are multithreaded processes. These processes allow the execution of multiple parts of a program at the same time. These are lightweight processes available within the process

## Parallel programming in Python using Pool class
- Another and more convenient approach for simple parallel processing tasks is provided by the Pool class.
- There are four methods that are particularly interesting:
	- Pool.apply
	- Pool.map
	- Pool.apply_async
	- Pool.map_async
- The **Pool.apply** and **Pool.map** methods are basically equivalents to Pythons in-built apply and map functions.
- 
## Reference Links
### Multiprocessing application development
- https://www.geeksforgeeks.org/multiprocessing-python-set-1/
- https://www.journaldev.com/15631/python-multiprocessing-example
- https://www.youtube.com/watch?v=5dMOYf0b_20

### Multitasking using thread
- https://www.geeksforgeeks.org/multithreading-python-set-1/

### Thread Synchronisation techniques
- https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/

### Parallel programming in Python using Pool class
- https://sebastianraschka.com/Articles/2014_multiprocessing.html#the-pool-class
- https://www.youtube.com/watch?v=u2jTn-Gj2Xw
- https://www.youtube.com/watch?v=fKl2JW_qrso