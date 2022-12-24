'''
In Python function is a group of related statement that perform a specific task.
Function help break our program into smaller and modular chunks. As our program grows larger and larger functions make it more organized and manageable.

> Categories of Function in Python
1. Built-in
2. Modules
3. User-defined

> Modules -> A module is a file containing functions and variables defined in separate files. A module is simply a file that contains Python code. When we break a program into modules, each module should contain functions that perfrom related tasks.
'''
import math as m  # import moodule

# from math import cos, sin
# even we don't need to import the hole module, we can import a specific component of the module like above.

from math import *
# Using above line we can import entire component of the math module.

print(m.pi)
print(cos(5))
print(sin(3.14))


# User-defined Functions

def greet():
    print("Hello Somnath")


greet()


def greeting(name, dish):
    print("Hello", name)
    print("Here is your", dish)


greeting("Arghya", "Pasta")


def meal(dish="rice"):  # default parameter
    print("Here is your next dish", dish)


meal()


def sum_of_list(a):
    print("Calculating...")
    return sum(a)


marks = [23, 45, 6, 23, 56, 74, 45]
sum_of_marks = sum_of_list(marks)

print("My sum of marks", sum_of_marks)
