# LinkedList Data Structure in Python

A simple implementation of a singly linked list in Python. 
This project demonstrates basic data structure implementation, 
iterator support, and unit testing using `unittest`.

---

## Overview

The `LinkedList` class provides a basic implementation of a singly linked list 
with a variety of operations:

- **Adding and inserting values**  
- **Removing values** (by value or by index)  
- **Searching for values and updating values**  
- **Iterating through list elements**

Each operation is tested with comprehensive unit tests to ensure correct 
functionality and proper error handling.

---

## Installation

 **Clone the Repository**  
   bash
   git clone https://github.com/superspartan6/linkedlist.git
   cd linkedlist


---

## Usage

Below is an example script demonstrating how to use the `LinkedList` class in your Python projects.

```python
from linkedlist import LinkedList

# Create an instance of LinkedList
ll = LinkedList()

# Add values to the list
ll.add_value(10)
ll.add_value(20)

# Insert a value at a specific index (insert 15 at index 1)
ll.insert_value(1, 15)

# Output the list as a standard Python list
print(ll.return_list())  # Expected Output: [10, 15, 20]

# Iterate through the linked list and print each value
for value in ll:
    print(value)
```
---

## Features

### Dynamic Operations
- **Add Value:** `add_value(value)`  
  *Adds a new element to the end of the linked list.*
- **Insert Value:** `insert_value(index, value)`  
  *Inserts a new element at the specified index.*
- **Remove Value:**  
  - `remove_first_value(value)` – *Removes the first occurrence of a value.*  
  - `remove_all_value(value)` – *Removes all occurrences of a value.*
- **Remove by Index:** `remove_index(index)`  
  *Removes the element at the specified index.*
- **Update Value:** `update_index(index, value)`  
  *Updates the element at the specified index with a new value.*
- **Search Operations:**  
  - `search_value(value)` – *Returns the index of the first matching value.*  
  - `search_all_value(value)` – *Returns a list of indices for all matching values.*  
  - `search_index(index)` – *Returns the value at the specified index.*
- **Get Size:** `get_size()`  
  *Returns the total number of elements in the list.*
- **Return List Representation:** `return_list()`  
  *Returns a standard Python list of all linked list elements.*

### Additional Features
- **Iterator Support:**  
  Implements the iterator protocol, allowing you to loop through the list easily using a for-loop.
- **Error Handling:**  
  Methods raise exceptions with the message `"Out of range"` when invalid indices are provided.
- **Unit Testing:**  
  Comprehensive tests using Python’s built-in `unittest` framework verify that all operations behave as expected.

---
## Contact

For questions, suggestions, or feedback, feel free to reach out via one of the following methods:

- **Email:** [caleb.zierenberg@gmail.com](mailto:caleb.zierenberg@gmail.com)
- **GitHub:** [superspartan6](https://github.com/superspartan6)
- **LinkedIn:** [Caleb Zierenberg](https://linkedin.com/in/calebzierenberg)

