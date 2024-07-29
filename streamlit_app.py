import streamlit as st

st.set_page_config(page_title='Python', layout='wide')

st.title("Python - CheatSheet")

_, exp_col, _ = st.columns([1, 3, 1])
with exp_col:
    with st.expander("**📖 How to use this CheatSheet?**"):
        st.markdown("""
                    The Python cheat sheet is a one-page reference sheet for the Python 3 programming language.

                    A popular programming language. Python can be used on a server to create web applications.
                    """)
        
        st.info("""
                This application is only secondary to the official Python documentation and serves as a quick guide through code snippets to learn Python. Official documentation [here.](https://www.python.org/)
                """)

# Add a welcome message
st.sidebar.markdown("""
    ## Welcome!
    Explore the Python Cheatsheet and learn various concepts and functionalities of Python.
    Use the navigation below to get started.
""")

# Add navigation instructions
st.sidebar.markdown("""
    ### How to Use
    - Use the sections below to quickly navigate through different topics.
    - Click on any section to view code snippets and explanations.
    - For any questions or feedback, feel free to reach out!
""")

# Add sidebar title
st.sidebar.title("Python Cheatsheet 📄")

# Function to display a code block section
def st_code_block(section_id, title, description, code):
    st.markdown(f"<div id='{section_id}'></div>", unsafe_allow_html=True)
    st.header(title)
    st.markdown(description)
    st.code(code, language='python')
    st.markdown("---")

# Getting Started
st_code_block("getting-started", "Getting Started", 
"""
**Hello World**
""", 
"""
print("Hello, World!")
# Hello, World!
""")

# Variables
st_code_block("variables", "Variables", 
"""
Variables can be assigned values of different types.
""",
"""
age = 18      # age is of type int
name = "John" # name is now of type str
print(name)
# Python can't declare a variable without assignment.
""")

# Data Types
st_code_block("data-types", "Data Types", 
"""
**str**: Text  
**int, float, complex**: Numeric  
**list, tuple, range**: Sequence  
**dict**: Mapping  
**set, frozenset**: Set  
**bool**: Boolean  
**bytes, bytearray, memoryview**: Binary  
See: [Data Types](https://docs.python.org/3/library/stdtypes.html)
""", 
"""
# Example of each data type:

# String
text = "Hello"

# Integer
integer = 42

# Float
floating_point = 3.14

# Complex
complex_number = 1 + 2j

# List
my_list = [1, 2, 3]

# Tuple
my_tuple = (1, 2, 3)

# Set
my_set = {1, 2, 3}

# Dictionary
my_dict = {"a": 1, "b": 2}

# Boolean
my_bool = True
""")

# Slicing String
st_code_block("slicing-string", "Slicing String", 
"""
Slice a string to get a substring.
""",
"""
msg = "Hello, World!"
print(msg[2:5])
# llo

print(msg[:5])
# Hello

print(msg[7:])
# World!
""")

# Lists
st_code_block("lists", "Lists", 
"""
Lists are mutable sequences, typically used to store collections of homogeneous items.
See: [Lists](https://docs.python.org/3/tutorial/datastructures.html)
""", 
"""
mylist = [1, 2, 3]
mylist.append(4)
mylist.insert(0, 0)
print(mylist) # => [0, 1, 2, 3, 4]

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
""")

# If Else
st_code_block("if-else", "If Else", 
"""
Basic control flow statement.
See: [Flow Control](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
""", 
"""
num = 200
if num > 0:
    print("num is greater than 0")
elif num == 0:
    print("num is zero")
else:
    print("num is less than 0")
""")

# Loops
st_code_block("loops", "Loops", 
"""
Loop through a sequence of numbers.
See: [Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
""", 
"""
# For Loop
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Finally finished!")

# While Loop
count = 0
while count < 3:
    print(count)
    count += 1
""")

# Functions
st_code_block("functions", "Functions", 
"""
Define and call a function.
See: [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
""", 
"""
def my_function(name):
    return f"Hello, {name}!"

print(my_function("Alice"))
# Hello, Alice!

# Lambda Function
square = lambda x: x**2
print(square(5))
# 25
""")

# File Handling
st_code_block("file-handling", "File Handling", 
"""
Open a file and read its contents.
See: [File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
""", 
"""
with open("myfile.txt", "w", encoding='utf8') as file:
    file.write("Hello, World!")

with open("myfile.txt", "r", encoding='utf8') as file:
    content = file.read()
    print(content)
# Hello, World!
""")

# Arithmetic
st_code_block("arithmetic", "Arithmetic", 
"""
Perform basic arithmetic operations.
""", 
"""
result = 10 + 30 # => 40
result = 40 - 10 # => 30
result = 50 * 5  # => 250
result = 16 / 4  # => 4.0 (Float Division)
result = 16 // 4 # => 4 (Integer Division)
result = 25 % 2  # => 1
result = 5 ** 3  # => 125

# Absolute Value
abs_value = abs(-10)
print(abs_value)
# 10
""")

# Plus-Equals
st_code_block("plus-equals", "Plus-Equals", 
"""
Use `+=` to add and assign in one step.
""", 
"""
counter = 0
counter += 10           # => 10
counter = 0
counter = counter + 10  # => 10

message = "Part 1."
message += " Part 2."    # => Part 1. Part 2.

# Other Operations
x = [1, 2, 3]
x *= 2
print(x)
# [1, 2, 3, 1, 2, 3]
""")

# f-Strings (Python 3.6+)
st_code_block("f-strings", "f-Strings (Python 3.6+)", 
"""
Use f-strings to format strings.
See: [Python F-Strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
""", 
"""
website = 'Quickref.ME'
greeting = f"Hello, {website}"
print(greeting)
# Hello, Quickref.ME

num = 10
formatted_string = f'{num} + 10 = {num + 10}'
print(formatted_string)
# 10 + 10 = 20
""")

# Built-in Data Types
st_code_block("strings", "Strings", 
"""
String literals can be enclosed in matching single quotes (') or double quotes (").
See: [Strings](https://docs.python.org/3/library/string.html)
""", 
"""
hello = "Hello World"
hello = 'Hello World'

multi_string = \"\"\"Multiline Strings
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.\"\"\"
print(multi_string)
""")

st_code_block("numbers", "Numbers", 
"""
Numbers in Python are of type int, float, or complex.
""", 
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
# <class 'int'>
""")

st_code_block("booleans", "Booleans", 
"""
Boolean values in Python.
""", 
"""
my_bool = True 
my_bool = False

print(bool(0)) # => False
print(bool(1)) # => True
""")

st_code_block("lists", "Lists", 
"""
Lists are mutable sequences, typically used to store collections of homogeneous items.
See: [Lists](https://docs.python.org/3/tutorial/datastructures.html)
""", 
"""
list1 = ["apple", "banana", "cherry"]
list2 = [True, False, False]
list3 = [1, 5, 7, 9, 3]
list4 = list((1, 5, 7, 9, 3))
print(list1[1])  # => banana
""")

st_code_block("tuples", "Tuple", 
"""
Tuples are immutable sequences, typically used to store collections of heterogeneous data.
""", 
"""
my_tuple = (1, 2, 3)


print(my_tuple[1])
# 2

a, b, c = my_tuple
print(a, b, c)
# 1 2 3
""")

st_code_block("sets", "Set", 
"""
Sets are unordered collections of unique items.
""", 
"""
set1 = {"a", "b", "c"}   
print(set1)

# Adding and Removing Items
set1.add("d")
set1.remove("b")
print(set1)
""")

st_code_block("dictionaries", "Dictionary", 
"""
Dictionaries are mutable mappings of keys to values.
""", 
"""
empty_dict = {}
a = {"one": 1, "two": 2, "three": 3}
print(a["one"])  # 1
print(a.keys())  # dict_keys(['one', 'two', 'three'])
print(a.values())# dict_values([1, 2, 3])
a.update({"four": 4})
print(a.keys())  # dict_keys(['one', 'two', 'three', 'four'])
print(a['four']) # 4
""")

# Casting
st_code_block("casting", "Casting", 
"""
Convert values from one type to another.
""", 
"""
# Integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
""")

# Advanced Data Types
st_code_block("heaps", "Heaps", 
"""
Heaps are binary trees for which every parent node has a value less than or equal to any of its children. Useful for accessing min/max value quickly.
See: [Heapq](https://docs.python.org/3/library/heapq.html)
""", 
"""
import heapq

myList = [9, 5, 4, 1, 3, 2]
heapq.heapify(myList) # turn myList into a Min Heap
print(myList)    # => [1, 3, 2, 5, 9, 4]

heapq.heappush(myList, 10)  # add 10 to the Min Heap
print(myList)    # => [1, 3, 2, 5, 9, 4, 10]

smallest = heapq.heappop(myList) # remove the smallest element
print(smallest, myList)  # => 1 [2, 3, 4, 5, 9, 10]
""")

# Math Operations
st_code_block("math", "Math Operations", 
"""
Python's math module provides many mathematical functions.
See: [Math Module](https://docs.python.org/3/library/math.html)
""", 
"""
import math

print(math.sqrt(16)) # Square root
# 4.0

print(math.pow(2, 3)) # Power
# 8.0

print(math.factorial(5)) # Factorial
# 120
""")

# Random Numbers
st_code_block("random", "Random Numbers", 
"""
Python's random module can be used to generate random numbers.
See: [Random Module](https://docs.python.org/3/library/random.html)
""", 
"""
import random

print(random.randint(1, 10)) # Random integer between 1 and 10
# prints a random integer between 1 and 10

myList = ['apple', 'banana', 'cherry']
print(random.choice(myList)) # Random choice from the list
# prints a random item from the list

print(random.sample(myList, 2)) # Random sample of 2 items
# prints a list with 2 random items
""")

# Dates
st_code_block("dates", "Dates", 
"""
Python's datetime module can be used to handle dates and times.
See: [Datetime Module](https://docs.python.org/3/library/datetime.html)
""", 
"""
import datetime

current_time = datetime.datetime.now()
print(current_time)
# 2023-01-01 12:00:00

# Date Formatting
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
# 2023-01-01 12:00:00
""")

# Regular Expressions
st_code_block("regex", "Regular Expressions", 
"""
Python's re module can be used to work with regular expressions.
See: [Regular Expressions](https://docs.python.org/3/library/re.html)
""", 
"""
import re

pattern = r'\b\w{3}\b'
text = 'One two three four five six'

matches = re.findall(pattern, text)
print(matches)
# ['One', 'two', 'six']

# Matching Patterns
match = re.search(r'\d+', 'The price is 100 dollars')
print(match.group())
# 100
""")

# JSON
st_code_block("json", "JSON", 
"""
Python's json module can be used to work with JSON data.
See: [JSON Module](https://docs.python.org/3/library/json.html)
""", 
"""
import json

json_data = '{"name": "John", "age": 30}'
parsed_data = json.loads(json_data)
print(parsed_data)
# {'name': 'John', 'age': 30}

python_data = {'name': 'John', 'age': 30}
json_string = json.dumps(python_data)
print(json_string)
# '{"name": "John", "age": 30}'
""")

# Decorators
st_code_block("decorators", "Decorators", 
"""
Decorators are a way to modify the behavior of a function or class.
See: [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
""", 
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Decorator with Arguments
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice! (repeated 3 times)
""")

# Web Scraping
st_code_block("web-scraping", "Web Scraping", 
"""
Python's BeautifulSoup module can be used to scrape data from web pages.
See: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
""", 
"""
import requests
from bs4 import BeautifulSoup

url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.string)
# Example Domain

# Extracting Links
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
""")

# Data Analysis
st_code_block("data-analysis", "Data Analysis", 
"""
Pandas is a popular data analysis library in Python.
See: [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)
""", 
"""
import pandas as pd

data = {'name': ['John', 'Anna', 'Peter'], 'age': [28, 24, 35]}
df = pd.DataFrame(data)

print(df)
#    name  age
# 0  John   28
# 1  Anna   24
# 2  Peter  35

# DataFrame Operations
df['age'] += 1
print(df)
#    name  age
# 0  John   29
# 1  Anna   25
# 2  Peter  36
""")

# Machine Learning
st_code_block("machine-learning", "Machine Learning", 
"""
Scikit-learn is a popular machine learning library in Python.
See: [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)
""", 
"""
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# Create and train the model
model = LinearRegression().fit(X, y)

# Make predictions
predictions = model.predict(np.array([[3, 5]]))
print(predictions)
# [16.]

# Model Coefficients
print("Coefficients:", model.coef_)
# Coefficients: [1. 2.]
""")

# Python Classes & Inheritance
st_code_block("defining-a-class", "Python Classes & Inheritance", 
"""
**Defining a Class**
""",
"""
class MyNewClass:
    pass

# Class Instantiation
my = MyNewClass()
""")

st_code_block("constructors", "Constructors", 
"""
**Constructor**
""",
"""
class Animal:
    def __init__(self, voice):
        self.voice = voice

cat = Animal('Meow')
print(cat.voice)    # => Meow

dog = Animal('Woof')
print(dog.voice)    # => Woof
""")

st_code_block("methods", "Methods", 
"""
**Methods**
""",
"""
class Dog:
    def bark(self):
        print("Ham-Ham")

charlie = Dog()
charlie.bark()   # => "Ham-Ham"
""")

st_code_block("class-variables", "Class Variables", 
"""
**Class Variables**
""",
"""
class MyClass:
    class_variable = "A class variable!"

print(MyClass.class_variable)  # => A class variable!

x = MyClass()
print(x.class_variable)       # => A class variable!
""")

st_code_block("super", "Super() Function", 
"""
**Super() Function**
""",
"""
class ParentClass:
    def print_test(self):
        print("Parent Method")

class ChildClass(ParentClass):
    def print_test(self):
        print("Child Method")
        super().print_test()

child_instance = ChildClass()
child_instance.print_test()
# Child Method
# Parent Method
""")

st_code_block("repr-method", "repr() Method", 
"""
**repr() Method**
""",
"""
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

john = Employee('John')
print(john)  # => John
""")

st_code_block("user-defined-exceptions", "User-Defined Exceptions", 
"""
**User-Defined Exceptions**
""",
"""
class CustomError(Exception):
    pass
""")

st_code_block("polymorphism", "Polymorphism", 
"""
**Polymorphism**
""",
"""
class ParentClass:
    def print_self(self):
        print('A')

class ChildClass(ParentClass):
    def print_self(self):
        print('B')

obj_A = ParentClass()
obj_B = ChildClass()

obj_A.print_self() # => A
obj_B.print_self() # => B
""")

st_code_block("overriding", "Overriding", 
"""
**Overriding**
""",
"""
class ParentClass:
    def print_self(self):
        print("Parent")

class ChildClass(ParentClass):
    def print_self(self):
        print("Child")

child_instance = ChildClass()
child_instance.print_self() # => Child
""")

st_code_block("inheritance", "Inheritance", 
"""
**Inheritance**
""",
"""
class Animal: 
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

class Dog(Animal):
    def sound(self):
        print("Woof!")

Yoki = Dog("Yoki", 4)
print(Yoki.name) # => Yoki
print(Yoki.legs) # => 4
Yoki.sound()     # => Woof!
""")

# Miscellaneous
st_code_block("comments", "Comments", 
"""
**Comments**
""",
"""
# This is a single line comment.

\"\"\" Multiline strings can be written
    using three "s, and are often used
    as documentation.
\"\"\"

''' Multiline strings can be written
    using three 's, and are often used
    as documentation.
'''
""")


st_code_block("generators", "Generators", 
"""
**Generators**
""",
"""
def double_numbers(iterable):
    for i in iterable:
        yield i + i

values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list) # => [-1, -2, -3, -4, -5]
""")

st_code_block("handle-exceptions", "Handle Exceptions", 
"""
**Handle Exceptions**
""",
"""
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass  # Multiple exceptions can be handled together, if required.
else:  # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")  # Runs only if the code in try raises no exceptions
finally:  # Execute under all circumstances
    print("We can clean up resources here")
""")

# Adding anchor links in the sidebar
st.sidebar.markdown("""
- [Getting Started](#getting-started)
- [Variables](#variables)
- [Data Types](#data-types)
- [Slicing String](#slicing-string)
- [Lists](#lists)
- [If Else](#if-else)
- [Loops](#loops)
- [Functions](#functions)
- [File Handling](#file-handling)
- [Arithmetic](#arithmetic)
- [Plus-Equals](#plus-equals)
- [f-Strings (Python 3.6+)](#f-strings-python-36)
- [Built-in Data Types](#built-in-data-types)
- [Casting](#casting)
- [Advanced Data Types](#advanced-data-types)
- [Math Operations](#math)
- [Random Numbers](#random)
- [Dates](#dates)
- [Regular Expressions](#regex)
- [JSON](#json)
- [Decorators](#decorators)
- [Web Scraping](#web-scraping)
- [Data Analysis](#data-analysis)
- [Machine Learning](#machine-learning)
- [Python Classes & Inheritance](#classes-inheritance)
- [Miscellaneous](#comments)
""")

st.sidebar.markdown("**Python Class & Inheritance**")
st.sidebar.markdown("""
- [Defining Classes](#defining-a-class)
- [Constructors](#constructors)
- [Methods](#methods)
- [Class Variables](#class-variables)
- [Super() Function](#super-function)
- [repr() Method](#repr-method)
- [User-Defined Exceptions](#user-defined-exceptions)
- [Polymorphism](#polymorphism)
- [Overriding](#overriding)
- [Inheritance](#inheritance)
""")

st.sidebar.markdown("**Miscellaneous**")
st.sidebar.markdown("""
- [Comments](#comments)
- [Generators](#generators)
- [Handle Exceptions](#handle-exceptions)
""")

# Footer
st.markdown("""
    <style>
    .footer {
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
        border-top: 1px solid #ddd;
        position: relative;
        bottom: 0;
    }
    .footer a {
        color: #1f77b4;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .footer img {
        vertical-align: middle;
        width: 20px;
        height: 20px;
        margin-left: 5px;
    }
    </style>
    <div class="footer">
        <p>Built with ❤️ by Shivang. | <a href="https://github.com/shivangraikar" target="_blank">
        <img src="https://img.icons8.com/material-outlined/24/000000/github.png" alt="GitHub"/> GitHub</a> - Feel free to open PRs!</p>
    </div>
    """, unsafe_allow_html=True)