# General Python info

## Packaging

| Reference/article/book | description  |
|--|--|
| [Structure of a Python program](https://docs.python-guide.org/writing/structure/) | Gives a good overview of how a Python program should be structured (docs.python-guide.org/writing) |
| [How to package your Python Code](https://python-packaging.readthedocs.io/en/latest/index.html) | This tutorial aims to put forth an opinionated and specific pattern to make trouble-free packages for community use |
| [Python Packaging from Init to Deploy](https://www.youtube.com/watch?v=4fzAMdLKC5k) | Youtube video that explains about setuptools, git, travis, readthedocs, PyPI |
| [Inside the Cheeseshop: How Python Packaging Works - PyCon 2018](https://www.youtube.com/watch?v=AQsZsgJ30AE) | Good history of Python related packaging solutions and issues |

## Python internals

| Reference/article/book | description  |
|--|--|
| [C for Yourself: Exploring Python Internals at the REPL (PyTexas 2017)](https://www.youtube.com/watch?v=zhvnyGd0n8Q) | Talks about some basic memory management aspects of Python by relating to the Python implementation in C (Interning) |
| [C for Yourself: Exploring Python Internals at the REPL (PyTexas 2017)](https://www.youtube.com/watch?v=zhvnyGd0n8Q) | Advanced Python topics  04:21 Python Design 05:29 Function creation 08:05 Class creation 10:48 Python scoping 13:13 Python modules 14:43 Python  Objects 19:15 Python Types (in C) 22:07 Python Classes in Python) 26:32 Iterators 28:32 Generators 33:28 Decorators 38:04 New-style classes 40:23 Descriptors 42:00 Properties 42:27 Class methods and static methods 46:23 \_\_slots\_\_ 48:00 \_\_new\_\_ 52:55 meta classes 01:00:43 multiple inheritance 01:05:00 Unicode |

## Data structures

| Reference/article/book | description  |
|--|--|
| [All Your Ducks In A Row: Data Structures in the Std Lib and Beyond - PyCon 2014](https://www.youtube.com/watch?v=fYlnfvKVDoM) | Talk about data structures and the effect its usage has on performance (arrays, lists, dicts, sets) |
| [PyCon 2010: The Mighty Dictionary](https://www.youtube.com/watch?v=C4Kc8xzcA68) | Talk about data structures and the effect its usage has on performance (arrays, lists, dicts, sets) |

## Typing

| Reference/article/book | description  |
|--|--|
| [What is Gradual Typing - 2014](http://wphomes.soic.indiana.edu/jsiek/what-is-gradual-typing/) | Gradual typing is a type system I developed with Walid Taha in 2006 that allows parts of a program to be dynamically typed and other parts to be statically typed. The programmer controls which parts are which by either leaving out type annotations or by adding them in. This article gives a gentle introduction to gradual typing |
| [Python Type Checking (Guide)](https://realpython.com/python-type-checking/#duck-types-and-protocols) | n this guide, you will get a look into Python type checking. Traditionally, types have been handled by the Python interpreter in a flexible but implicit way. Recent versions of Python allow you to specify explicit type hints that can be used by different tools to help you develop your code more efficiently |

## Productivity & tools

| Reference/article/book | description  |
|--|--|
| [Dan Taylor - Get Productive with Python in Visual Studio Code]([https://www.youtube.com/watch?v=6YLMWU-5H9o](https://www.youtube.com/watch?v=6YLMWU-5H9o)) | Walkthrough of main features of the Python Extension libary for Visual Code |

## Functional programming

| Reference/article/book | description  |
|--|--|
| [Functional Programming with Python for People Without Time]([https://medium.com/@jondot/functional-programming-with-python-for-people-without-time-1eebdbd9526c) | Functional programming for the purpose of this article (and I claim — for the purpose of most of your day to day work), is all about building pipelines and moving data through those pipelines |

## Reactive programming
| Reference/article/book | description  |
|--|--|
| [The Reactive Extensions for Python (RxPY)]([https://github.com/ReactiveX/RxPY) | Reactive Extensions for Python (RxPY) is a set of libraries for composing asynchronous and event-based programs using observable sequences and pipable query operators in Python 

## Classes
| Reference/article/book | description  |
|--|--|
| [Spreading a Class Over Multiple Files]([https://medium.com/@jondot/functional-programming-with-python-for-people-without-time-1eebdbd9526c) | What happens if our class has some very large methods? Or lots or methods? Or both? Personally, I prefer to keep my modules under 1,000 lines, but larger classes—such as those that provide an application's data storage or a top-level window in a GUI application—can easily run to well over 1,000 lines. Fortunately, thanks to Python's flexibility and meta-programming support (don't worry, the code is short and straightforward!) we can keep our modules to a managable size by spreading a class over as many files as we like |
