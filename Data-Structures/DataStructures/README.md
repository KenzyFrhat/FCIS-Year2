# Linked List–Based Data Structures in Python

This project provides clean and structured **Python implementations** of fundamental data structures built **entirely using linked lists**, without relying on Python’s built-in containers such as `list` or `deque`.

The goal is to demonstrate how multiple abstract data types can be derived from linked list foundations using **object references** as pointer equivalents.

---

## Implemented Data Structures

### 1. Singly Linked List
A linear data structure where each node contains:
- A data value
- A reference to the next node

**Characteristics:**
- One-directional traversal
- Dynamic memory allocation
- Efficient insertions and deletions

---

### 2. Doubly Linked List
An extension of the singly linked list where each node contains:
- A reference to the next node
- A reference to the previous node

**Characteristics:**
- Bidirectional traversal
- Easier node removal
- Slightly higher memory usage

---

### 3. Stack (Linked List–Based)
A **Last-In, First-Out (LIFO)** data structure implemented using a linked list.

**Core operations:**
- `push`
- `pop`
- `peek`
- `is_empty`

**Design note:**
All operations are performed at the head of the linked list to ensure constant-time complexity.

---

### 4. Queue (Linked List–Based)
A **First-In, First-Out (FIFO)** data structure implemented using a linked list.

**Core operations:**
- `enqueue`
- `dequeue`
- `front`
- `is_empty`

**Design note:**
Maintains references to both front and rear nodes for efficient operations.

---

### 5. Circular Queue (Linked List–Based)
A queue implementation where:
- The last node links back to the first node
- The structure forms a logical circle

**Characteristics:**
- No wasted space
- Efficient enqueue and dequeue
- Continuous traversal capability

---

## Project Objectives

- Implement classical data structures **from scratch in Python**
- Understand pointer-like behavior using object references
- Reinforce object-oriented design principles
- Practice clean separation between data structures

---

## Technologies Used

- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming
- **Restrictions:** No use of built-in data structures for internal storage

---

## Usage

Each data structure is implemented in a separate Python module and can be imported and tested independently.

Example usage patterns are kept minimal to emphasize internal structure design.

---

## Educational Purpose

This project is intended for **learning and academic practice** in data structures and algorithms, focusing on clarity, correctness, and conceptual understanding rather than performance optimization.

---

## Author

Developed as part of a **Data Structures** course using Python.
