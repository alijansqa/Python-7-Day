# Python 7-Day Challenge — Day 7: Core OOP & Advanced Fundamentals

This directory contains scripts and lab exercises covering advanced Object-Oriented Programming (OOP) concepts, Exception Handling, Modules & Package Management (`pip`), File Handling (I/O), and PyCharm Debugging techniques.

---

## 📁 Repository Structure & Lab Overview

| File Name | Topic Covered | Summary / Description |
| :--- | :--- | :--- |
| **`Lab048.py`** | Abstraction | Hiding implementation details and exposing essential interfaces (`Car` class example)[cite: 8]. |
| **`Lab049.py`** | Polymorphism & Operator Overloading | Redefining default behavior for operators (`+`) and dunder methods across custom types[cite: 9]. |
| **`Lab050.py`** | Exception Handling (Basics) | Preventing program crashes using `try-except` blocks for unpredictable input[cite: 10]. |
| **`Lab051.py`** | Exception Handling (Clean Flow) | Executing cleanup blocks and custom error handling without breaking workflow execution[cite: 11]. |
| **`Lab052.py`** | Multiple Exception Types | Catching specific runtime errors such as `ValueError` and `IndexError`[cite: 12]. |
| **`Lab053.py`** | Modules & `pip` | Understanding built-in vs external libraries, package installation via `pip`, and module imports[cite: 13]. |
| **`Lab054.py`** | File I/O (File Handling) | Reading, writing, appending files, and using context managers (`with open()`) safely[cite: 14]. |
| **`Lab055.py`** | PyCharm Debugging | Setting breakpoints, inspecting variables, stepping line-by-line (`F8`), and analyzing execution flow[cite: 15]. |

---

## 🔑 Key Concepts Summarized

### 1. Object-Oriented Programming (OOP) Pillars
* **Abstraction:** Hides underlying complex implementation details (e.g., ignition, clutch, and acceleration mechanics inside a `Car` object) to show only relevant actions to the caller[cite: 8].
* **Polymorphism:** Allows operators or functions to exhibit different behaviors depending on operand data types or custom dunder definitions[cite: 9].

### 2. Error & Exception Handling
* Wrapped vulnerable script execution blocks inside `try` structures to gracefully intercept runtime failures[cite: 10, 11].
* Explicitly filtered distinct error classes (e.g., `ValueError` for bad type casting, `IndexError` for out-of-bounds list index access) to optimize failure recovery[cite: 12].

### 3. Modules & Package Management
* **Modules:** Modular Python scripts holding reusable methods and variables to promote DRY (Don't Repeat Yourself) code architecture[cite: 13].
* **`pip`:** Python's standard package manager used to install third-party testing libraries (e.g., `pip install pandas`, `pip install selenium`)[cite: 13].

### 4. File Handling (I/O)
* **File Operations:** Evaluated key opening modes:
  * `'r'` — Read-only mode (raises an error if the target file does not exist)[cite: 14].
  * `'w'` — Write mode (creates a new file or overwrites existing file content)[cite: 14].
  * `'a'` — Append mode (appends data to the end of the file without overwriting)[cite: 14].
* **Context Manager (`with open`):** Automatically closes open file streams upon completion to prevent resource locking and memory leakage[cite: 14].

### 5. Debugging
* Managed execution flow by assigning line breakpoints, inspecting variable state values step-by-step using `F8`, and identifying scope logic errors during execution[cite: 15].

---

## 🛠 Tech Stack & Environment
* **Language:** Python 3.14.8
* **IDE:** JetBrains PyCharm
* **Version Control:** Git & GitHub
