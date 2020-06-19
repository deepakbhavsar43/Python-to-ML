
# History of Python
- The history of Python starts with the programming language ABC.
- ABC is a general-purpose programming language and programming environment, which had been developed in the Netherlands,Amsterdam, at the CWI (CentrumWiskunde & Informatica).
- The greatest achievement of ABC was to influence the design of Python.
- Python was conceptualized in the late 1980s. Guido van Rossum worked that time in a project at the CWI, called Amoeba, a distributed operating system
- He programmed in ABC.
- Van Rossum shouldered sole responsibility for the project, as the lead developer, until July 12, 2018, when he announced his "permanent vacation" from his responsibilities
- In an interview with BillVenners (January 2003), Guido van Rossum said: "I remembered all my experience and some of my frustration with ABC.
- I decided to try to design a simple scripting language that possessed some of ABC's better properties, but without its problems.
- In January, 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" to lead the project.

- Python 2.0 was released on 16 October 2000 with many major new features, including a [cycle-detecting](https://en.wikipedia.org/wiki/Cycle_detection "Cycle detection")  [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science) "Garbage collection (computer science)") and support for [Unicode](https://en.wikipedia.org/wiki/Unicode). 
  - The Python 2 language, i.e. Python 2.7.x, is officially being discontinued on January 1, 2020 (first planned for 2015) after which security patches and other improvements will not be released for it.
- Python 3.0, released in 2008, was a major revision of the language that is not completely [backward-compatible](https://en.wikipedia.org/wiki/Backward_compatibility "Backward compatibility"), and much Python 2 code does not run unmodified on Python 3.
#  Python Introduction

 - Python is a **dynamic**, **general-purpose**, **interpreted** high-level programming language whose design philosophy emphasizes code readability.
 - There are **no type declaration**s of variables, parameters, functions, or methods in source code.
 - Python has a large and comprehensive standard library.
 - This makes the code **short** and **flexible**
 - Python interpreters are available for many operating systems.
 
 An excellent way to see how Python code works is to run the Python interpreter and type code right into it. 

If you ever have a question like, "What happens if I add an `int` to a `list`?" Just typing it into the Python interpreter is a fast and likely the best way to see what happens. (See below to see what really happens!)
```sh
$ python ## Run the Python interpreter  
Python  2.7.9  (default,  Dec  30  2014,  03:41:42)  [GCC 4.1.2  20080704  (Red  Hat  4.1.2-55)] on linux2Type  "help",  "copyright",  "credits"  or  "license"  for more information.  
>>> a =  6  ## set a variable in this interpreter session  
>>> a ## entering an expression prints its value  
6  
>>> a +  2  
8  
>>> a =  'hi'  ## 'a' can hold a string just as well  
>>> a'hi'  
>>> len(a)  ## call the len() function on a string  
2  
>>> a + len(a)  ## try something that doesn't work  
Traceback  (most recent call last):  File  "", line 1,  in    
TypeError: cannot concatenate 'str'  and  'int' objects>>> a + str(len(a))  ## probably what you really wanted  
'hi2'  
>>> ## try something else that doesn't work  
Traceback  (most recent call last):  File  "", line 1,  in    
NameError: name 'foo'  is  not  defined  
>>> ## type CTRL-d to exit (CTRL-z in Windows/DOS terminal)
```
- the interpreter throws a run-time error if the code tries to read a variable that has not been assigned a value.
- Like C++ and Java, Python is case sensitive so "a" and "A" are different variables.
- unlike C++ and Java, Python does not require a semicolon at the end of each statement.
- Comments begin with a '#'

# Alternative Python Implementations

-   [IronPython](http://ironpython.net/)  (Python running on .NET)
-   [Jython](http://www.jython.org/)  (Python running on the Java Virtual Machine)
-   [PyPy](http://pypy.org/)  (A  [fast](http://speed.pypy.org/)  python implementation with a JIT compiler)
-   [Stackless Python](http://www.stackless.com/)  (Branch of CPython supporting microthreads)
-   [MicroPython](http://micropython.org/)  (Python running on micro controllers)

Other parties have re-packaged CPython. These re-packagings often include more libraries or are specialized for a particular application:

-   [ActiveState ActivePython](http://www.activestate.com/activepython/)  (commercial and community versions, including scientific computing modules)
-   [pythonxy](http://python-xy.github.io/)  (Scientific-oriented Python Distribution based on Qt and Spyder)
-   [winpython](http://winpython.github.io/)  (WinPython is a portable scientific Python distribution for Windows)
-   [Conceptive Python SDK](http://www.conceptive.be/python-sdk.html)  (targets business, desktop and database applications)
-   [Enthought Canopy](https://www.enthought.com/products/canopy/)  (a commercial distribution for scientific computing)
-   [PyIMSL Studio](http://www.roguewave.com/products/imsl-numerical-libraries/pyimsl-studio.aspx)  (a commercial distribution for numerical analysis – free for non-commercial use)
-   [Anaconda Python](https://www.anaconda.com/distribution/)  (a full Python distribution for data management, analysis and visualization of large data sets)
-   [eGenix PyRun](https://www.egenix.com/products/python/PyRun/)  (a portable Python runtime, complete with stdlib, frozen into a single 3.5MB - 13MB executable file)

If you want to host and run Python in the cloud, these implementations may be right for you:

-   [PythonAnywhere](https://www.pythonanywhere.com/)  (freemium hosted Python installation which lets you run Python in the browser, e.g. for tutorials, showcases, etc.)

# Features of Python
- Python provides lots of features that are listed below.
	-  Python is easy to learn and use. It is developer-friendly and high level programming language.
- Expressive Language
	- Python language is more expressive means that it is more understandable and readable.
-  Interpreted Language
	- Python is an interpreted language i.e. interpreter executes the code line by line at a time. This makes debugging easy and thus suitable for beginners.
-  Cross-platform Language
	- Python can run equally on different platforms such as Windows, Linux, Unix and Macintosh etc. So, we can say that Python is a portable language.
-  Free and Open Source
	- Python language is freely available at  [offical web address](https://www.python.org/).The source-code is also available. Therefore it is open source.
-  Object-Oriented Language
	- Python supports object oriented language and concepts of classes and objects come into existence.
-  Extensible
	- It implies that other languages such as C/C++ can be used to compile the code and thus it can be used further in our python code.
-  Large Standard Library
	- Python has a large and broad library and prvides rich set of module and functions for rapid application development.
-  GUI Programming Support
	- Graphical user interfaces can be developed using Python.
- Integrated
	- It can be easily integrated with languages like C, C++, JAVA etc.

# Python Version List

Python programming language is being updated regularly with new features and supports. There are lots of updations in python versions, started from 1994 to current release.

A list of python versions with its released date is given below.


| Python Version  | Released Date |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Python 1.0 | January 1994 |
| Python 1.5 | December 31, 1997 |
| Python 1.6 | September 5, 2000 |
| Python 2.0 | October 16, 2000 |
| Python 2.1 | April 17, 2001 |
| Python 2.2 | December 21, 2001 |
| Python 2.3 | July 29, 2003 |
| Python 2.4 | November 30, 2004 |
| Python 2.5 | September 19, 2006 |
| Python 2.6 | October 1, 2008 |
| Python 2.7 | July 3, 2010 |
| Python 3.0 | December 3, 2008 |
| Python 3.1 | June 27, 2009 |
| Python 3.2 | February 20, 2011 |
| Python 3.3 | September 29, 2012 |
| Python 3.4 | March 16, 2014 |
| Python 3.5 | September 13, 2015 |
| Python 3.6 | December 23, 2016 |
| Python 3.7 | June 27, 2018 |

# Tool Chain

 The standard implementation of python is called “**cpython**”. It is the default and widely used implementation of the Python.
 
 Python doesn't convert its code into machine code. It actually converts it into something called byte code.

 So within python, compilation happens, but its just not into a machine language. It is into **byte code** and this byte code can	t be understood by CPU. So we need actually an interpreter called the python virtual machine. The python virtual machine executes the byte codes.
![](https://media.geeksforgeeks.org/wp-content/uploads/python_working.png)

                
# Installation of Anaconda Distribution and other python IDE
## Installing Anaconda on Windows
1. Download the Anaconda installer.
2.  Verify data integrity with SHA-256.
	- We do not recommend using MD5 verification as SHA-256 is more secure.
	- If you have PowerShell V4 or later:
		 - Open a PowerShell console and verify the file as follows:
	```sh
	Get-FileHash filename -Algorithm SHA256
	```
	- If you dont have PowerShell V4 or later:
	Use the free online verifier tool on the Microsoft website.<br />
		(1) Download the file and extract it.<br />
		(2) Open a Command Prompt window.<br />
		(3) Navigate to the file.<br />
		(4) Run the following command:<br />
			Start-PsFCIV -Path C:pathtofile.ext -HashAlgorithm SHA256 -Online<br />
3. Double click the installer to launch.
4. Click Next.
5. Read the licensing terms and click “I Agree”.
6. Select an install for **Just Me** unless you are installing for all users (which requires Windows Administrator privileges) and click Next.
7. Select a destination folder to install Anaconda and click the Next button.
8. Choose whether to add Anaconda to your PATH environment variable. We recommend **not adding Anaconda to the PATH environment variable**, since this can interfere with other software. Instead, use Anaconda software by opening Anaconda Navigator or the Anaconda Prompt from the Start Menu.
9. Choose whether to register Anaconda as your default Python. Unless you plan on installing and running multiple versions of Anaconda or multiple versions of Python, accept the default and leave this box checked.
10. Click the **Install button**.
11. Click the Next button.
12. After a successful installation you will see the “Thanks for installing Anaconda” dialog box:
13. Click the **Finish** button.
14. Verify your installation.
	- Windows: Click Start, search or select Anaconda Navigator from the menu.

## Installing PyCharm on Windows
1. To download PyCharm visit the website https://www.jetbrains.com/pycharm/download/ and Click the **DOWNLOAD** link under the Community Section.
2. Once the download is complete, run the exe for install PyCharm. The setup wizard should have started. Click **Next**.
3. On the next screen, Change the installation path if required. Click **Next**.
4. On the next screen, you can create a desktop shortcut if you want and click on **Next**.
5. Choose the start menu folder. Keep selected JetBrains and click on **Install**.
6.  Wait for the installation to finish.
7.  Once installation finished, you should receive a message screen that PyCharm is installed. If you want to go ahead and run it, click the **Run PyCharm Community Edition box** first and click **Finish**.
8. After you click on "Finish," the Following screen will appear.
