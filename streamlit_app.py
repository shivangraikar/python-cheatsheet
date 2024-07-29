import streamlit as st

st.set_page_config(page_title='Python', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)

st.title("Python - CheatSheet")

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    with st.expander("**📖 How to use this CheatSheet?**"):
        st.markdown("""

                    The Python cheat sheet is a one-page reference sheet for the Python 3 programming language.

                    A popular programming language. Python can be used on a server to create web applications.
                    """)
        
        st.info("""
                This application is only secondary to the official Python documentation and serves as a quick guide through code snippets to learn Python. Offical documentation [here.](https://www.python.org/)
                """)

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
""", "")

# Slicing String
st_code_block("slicing-string", "Slicing String", 
"""
Slice a string to get a substring.
""",
"""
msg = "Hello, World!"
print(msg[2:5])
# llo
""")

# Lists
st_code_block("lists", "Lists", 
"""
Lists are mutable sequences, typically used to store collections of homogeneous items.
See: [Lists](https://docs.python.org/3/tutorial/datastructures.html)
""", 
"""
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item)
    # prints out 1,2
""")

# If Else
st_code_block("if-else", "If Else", 
"""
Basic control flow statement.
See: [Flow Control](https://docs.python.org/3/tutorial/controlflow.html)
""", 
"""
num = 200
if num > 0:
    print("num is greater than 0")
else:
    print("num is not greater than 0")
""")

# Loops
st_code_block("loops", "Loops", 
"""
Loop through a sequence of numbers.
See: [Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
""", 
"""
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Finally finished!")
""")

# Functions
st_code_block("functions", "Functions", 
"""
Define and call a function.
See: [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
""", 
"""
def my_function():
    print("Hello from a function")

my_function()
# Hello from a function
""")

# File Handling
st_code_block("file-handling", "File Handling", 
"""
Open a file and read its contents.
See: [File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
""", 
"""
with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)
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
message += "Part 2."    # => Part 1.Part 2.
""")

# f-Strings (Python 3.6+)
st_code_block("f-strings", "f-Strings (Python 3.6+)", 
"""
Use f-strings to format strings.
See: [Python F-Strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
""", 
"""
website = 'Quickref.ME'
f"Hello, {website}"
# "Hello, Quickref.ME"

num = 10
f'{num} + 10 = {num + 10}'
# '10 + 10 = 20'
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
consectetur adipiscing elit \"\"\"
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

bool(0)     # => False
bool(1)     # => True
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
""")

st_code_block("tuples", "Tuple", 
"""
Tuples are immutable sequences, typically used to store collections of heterogeneous data.
""", 
"""
my_tuple = (1, 2, 3)
my_tuple = tuple((1, 2, 3))
""")

st_code_block("sets", "Set", 
"""
Sets are unordered collections of unique items.
""", 
"""
set1 = {"a", "b", "c"}   
set2 = set(("a", "b", "c"))
""")

st_code_block("dictionaries", "Dictionary", 
"""
Dictionaries are mutable mappings of keys to values.
""", 
"""
empty_dict = {}
a = {"one": 1, "two": 2, "three": 3}
a["one"]
# 1
a.keys()
# dict_keys(['one', 'two', 'three'])
a.values()
# dict_values([1, 2, 3])
a.update({"four": 4})
a.keys()
# dict_keys(['one', 'two', 'three', 'four'])
a['four']
# 4
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

print(math.sqrt(16))
# 4.0

print(math.pow(2, 3))
# 8.0
""")

# Random Numbers
st_code_block("random", "Random Numbers", 
"""
Python's random module can be used to generate random numbers.
See: [Random Module](https://docs.python.org/3/library/random.html)
""", 
"""
import random

print(random.randint(1, 10))
# prints a random integer between 1 and 10

myList = ['apple', 'banana', 'cherry']
print(random.choice(myList))
# prints a random item from the list
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
""")

cols = st.columns(2)