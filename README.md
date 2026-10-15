# 🐍 Python Automation & SQA Engineering - 7-Day

A comprehensive, lab-based repository documenting core Python programming concepts, Object-Oriented Programming (OOP) architectures, file handling, exception management, and framework preparation for Software Quality Assurance (SQA) Automation Engineers.

---

## 🎯 Repository Purpose

This repository contains hands-on code scripts, practical exercises, and lab implementations completed over a 7-day intensive learning sprint. Built with an emphasis on **clean code, reusability, memory efficiency, and practical test engineering concepts**, these modules form the prerequisite foundation for web (Selenium/Playwright), API (Requests), and unit testing (PyTest) automation frameworks.

---

## 📅 Roadmap & Syllabus Breakdown

### 🟢 Day 1 – Day 3: Foundations & Control Logic
* **Python Environment & Syntax Basics:** Variables, primitive data types, memory references, and basic execution flow.
* **Operators & Expressions:** Arithmetic, logical, assignment, and comparison operators.
* **Control Structures:** `if-else` branching, conditional evaluation, loop constructs (`for`, `while`), `break`, and `continue`.

### 🟡 Day 4 – Day 5: Data Structures & Modular Functions
* **Core Collections:** Hands-on operations with `Lists`, `Tuples`, `Sets`, and `Dictionaries`.
* **Data Manipulation:** List comprehension, sequence slicing, key-value lookup strategies, and immutability rules.
* **Functions:** Function declaration, parameter passing (`*args`, `**kwargs`), return statements, and local/global scope management.

### 🟠 Day 6: Object-Oriented Programming (OOP Core)
* **Classes & Objects:** Blueprints, instantiation, and instance attributes (`__init__`).
* **Encapsulation:** Grouping data and methods, protecting internal states, and managing access levels (`_protected` and `__private` variables).
* **Static Methods:** Utility function design without relying on class instance context.

### 🔴 Day 7: Advanced OOP, Robustness & Tooling
* **Abstraction:** Hiding complex internal logic behind clean public interfaces (`Car` engine model)[cite: 8].
* **Polymorphism & Dunder Methods:** Operator overloading (`+`, `-`) and custom class behaviors using `__add__` and `__sub__`[cite: 9].
* **Exception Handling:** Preventing runtime crashes using structured `try-except-finally` blocks and intercepting specific errors (`ValueError`, `IndexError`)[cite: 10, 11, 12].
* **File I/O:** Reading, writing, appending files, and using context managers (`with open()`) for automated file lifecycle management[cite: 14].
* **Modules & `pip`:** Package management, library installations, and modular code imports[cite: 13].
* **PyCharm Debugging:** Setting breakpoints, line-by-line step execution (`F8`), and runtime variable state inspection.

---

## 📂 Project Structure & Lab Index

```text
.
├── DAY 1/
│   ├── Lab001.py        # Python syntax & Hello World
│   ├── Lab002.py        # Variables & dynamic typing
│   ├── Lab003.py        # Primitive data types (int, float, str, bool)
│   ├── Lab004.py        # User input handling & type conversions
│   ├── Lab005.py        # Formatting output & strings
│   ├── Lab006.py        # String methods & indexing
│   └── Lab007.py        # Practical basics & setup verification
│
├── DAY 2/
│   ├── Lab008.py        # Arithmetic & assignment operators
│   ├── Lab009.py        # Comparison & logical operators
│   ├── Lab010.py        # Bitwise operators & boolean logic
│   ├── Lab011.py        # Strings formatting & escape characters
│   ├── Lab012.py        # Mathematical operations & built-in functions
│   ├── Lab013.py        # Type casting & data validation
│   ├── Lab014.py        # Ternary operator & conditional expressions
│   └── Lab015.py        # Operator precedence & practical exercises
│
├── DAY 3/
│   ├── Lab016.py        # Basic if-else branching
│   ├── Lab017.py        # Nested conditional logic & edge cases
│   ├── Lab018.py        # Multiple condition evaluation (elif)
│   ├── Lab019.py        # For loop fundamentals & range() function
│   ├── Lab020.py        # While loop constructs & condition flags
│   ├── Lab021.py        # Loop control statements (break, continue)
│   ├── Lab022.py        # Pass statement & empty blocks
│   ├── Lab023.py        # Match-case statements (Python 3.10+)
│   └── Lab024.py        # Loop patterns & logic building
│
├── DAY 4/
│   ├── Lab025.py        # List creation, indexing & slicing
│   ├── Lab026.py        # List methods (append, insert, pop, remove)
│   ├── Lab027.py        # Tuple basics & immutability
│   ├── Lab028.py        # Set operations & uniqueness
│   ├── Lab029.py        # Set math (union, intersection, difference)
│   ├── Lab030.py        # Dictionary basics (keys, values, items)
│   ├── Lab031.py        # Dictionary methods & nested lookup
│   ├── Lab032.py        # List & dictionary comprehensions
│   └── Lab033.py        # Collection conversion & data manipulation
│
├── DAY 5/
│   ├── Lab034.py        # Function definition & execution flow
│   ├── Lab035.py        # Positional & default arguments
│   ├── Lab036.py        # Return statements & multiple returns
│   ├── Lab037.py        # Variable scope (local vs global)
│   ├── Lab038.py        # Arbitrary positional args (*args)
│   ├── Lab039.py        # Arbitrary keyword args (**kwargs)
│   ├── Lab040.py        # Lambda functions & anonymous calls
│   └── Lab041.py        # Built-in higher-order functions (map, filter)
│
├── DAY 6/
│   ├── Lab042.py        # Class blueprint & object instantiation
│   ├── Lab043.py        # Instance variables & constructor (__init__)
│   ├── Lab044.py        # Encapsulation basics & public attributes
│   ├── Lab045.py        # Private attributes (__var) & getters/setters
│   ├── Lab046.py        # Protected attributes (_var) & class variables
│   └── Lab047.py        # Static methods & utility functions
│
└── DAY 7/
    ├── __init__.py
    ├── Lab048.py        # Abstraction implementation
    ├── Lab049.py        # Polymorphism & operator overloading
    ├── Lab050.py        # Basic Exception Handling (try/except)
    ├── Lab051.py        # Clean exception handling & workflow continuity
    ├── Lab052.py        # Multi-exception handling (ValueError, IndexError)
    ├── Lab053.py        # Modules, imports, & pip package manager
    ├── Lab054.py        # File I/O operations & context managers
    └── Lab055.py        # PyCharm debugging & execution steps
