---
marp: true
theme: uncover
---

# Python Programming Language
## A Comprehensive Overview

---

# What is Python? 🐍

* High-level programming language
* Created by Guido van Rossum in 1991
* Known for its simplicity and readability
* Supports multiple programming paradigms
* Currently at version 3.12

---

# History & Evolution 📜

* Python 1.0 (1994)
* Python 2.0 (2000)
* Python 3.0 (2008)
* Major shift from Python 2 to 3
* Focus on Unicode and clean design

---

# Key Features ⭐

* **Easy to Read**: Clean and intuitive syntax
* **Interpreted**: No compilation needed
* **Dynamic Typing**: Flexible variable types
* **Large Standard Library**: "Batteries included"
* **Cross-platform**: Runs everywhere

---

# Python Philosophy 🤔

```python
import this
```

* Explicit is better than implicit
* Simple is better than complex
* Readability counts
* Flat is better than nested
* Practicality beats purity

---

# Basic Syntax 📝

```python
# Variables and data types
name = "Python"    # str
age = 32          # int
price = 3.14      # float
is_cool = True    # bool

# F-strings
print(f"{name} is {age} years old!")
```

---

# Data Structures 📊

```python
# Lists
fruits = ['apple', 'banana', 'orange']

# Dictionaries
person = {
    'name': 'John',
    'age': 30
}

# Tuples
coordinates = (10, 20)

# Sets
unique_numbers = {1, 2, 3, 3}  # {1, 2, 3}
```

---

# Control Flow 🔄

```python
# If statements
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Loops
for i in range(5):
    print(i)

while condition:
    # do something
```

---

# Functions 🎯

```python
# Basic function
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Lambda function
square = lambda x: x**2

# Args and kwargs
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
```

---

# Object-Oriented Programming 🎨

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"
    
    @property
    def is_adult(self):
        return self.age >= 18
```

---

# Exception Handling 🔧

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code")
```

---

# Context Managers 📂

```python
# File handling
with open('file.txt', 'r') as file:
    content = file.read()

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Time: {time.time() - start}s")
```

---

# Decorators 🎭

```python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_function
def example():
    pass
```

---

# Generator Functions 🔄

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci(10):
    print(num)
```

---

# Modern Python Features ✨

* Type hints
* Walrus operator (:=)
* f-strings
* Async/await
* Pattern matching
* Dataclasses

---

# Applications 🚀

* Web Development
  * Django, Flask, FastAPI
* Data Science & ML
  * NumPy, Pandas, Scikit-learn
* AI & Deep Learning
  * TensorFlow, PyTorch
* Automation & Scripting
* Game Development
  * Pygame, Panda3D

---

# Python Ecosystem 🌐

* **pip**: Package manager
* **virtualenv/venv**: Environment management
* **Jupyter**: Interactive computing
* **NumPy/Pandas**: Data analysis
* **Django/Flask**: Web frameworks
* **pytest**: Testing framework
* **black/pylint**: Code formatting

---

# Best Practices 📌

* Follow PEP 8 style guide
* Use virtual environments
* Write tests
* Document your code
* Use type hints
* Keep functions small
* Handle exceptions properly

---

# Development Tools 🛠️

* VSCode
* PyCharm
* Jupyter Notebooks
* Git integration
* Debuggers
* Linters and formatters

---

# Why Choose Python? 🤔

* Beginner-friendly
* Extensive community support
* Rich ecosystem of libraries
* Industry standard
* Versatile applications
* Great documentation
* Active community

---

# Learning Resources 📚

* [python.org](https://python.org)
* Real Python
* Python Documentation
* GitHub Repositories
* Online Courses
* PyCon talks
* Python Weekly newsletter

---

# Real-world Examples 💡

* Instagram (Django)
* Dropbox
* Netflix
* Spotify
* Reddit
* YouTube
* NASA

---

# Thank You! 👋

Questions?

Contact: example@email.com
GitHub: github.com/example

