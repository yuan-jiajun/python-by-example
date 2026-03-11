# 📚 Project 03: Library Management System

## Difficulty: 🟠 Advanced

## Description
Build an object-oriented Library Management System where users can manage books,
members, and borrowing/returning of books. This project emphasizes classes,
inheritance, encapsulation, and error handling.

## Requirements

1. Create a `Book` class with title, author, ISBN, and availability status
2. Create a `Member` class with name, member ID, and borrowed books list
3. Create a `Library` class that manages books and members
4. Allow adding/removing books from the library catalog
5. Allow registering new members
6. Implement borrow and return functionality with proper validation
7. Handle edge cases: book already borrowed, member limit reached, book not found
8. Display library catalog and member details

## Concepts You'll Practice

- Classes and Objects
- Inheritance and Encapsulation
- Properties and Methods
- Custom Exceptions
- `__str__` and `__repr__` magic methods
- Composition (Library has Books and Members)

## Example Output

```
📚 LIBRARY MANAGEMENT SYSTEM
=============================

1. View Catalog
2. Add Book
3. Register Member
4. Borrow Book
5. Return Book
6. View Member Info
7. Exit

Choose: 4

Enter Member ID: M001
Enter Book ISBN: 978-0-13-110362-7

✅ "The C Programming Language" has been borrowed by Alice.
   Due date: 2025-02-15
   Books borrowed: 1/3
```

## How to Run

```bash
cd projects/03_library_management
python solution.py
```

## Bonus Challenges

- [ ] Add due dates and overdue book tracking
- [ ] Save library data to JSON for persistence
- [ ] Add search functionality (by title, author, or ISBN)
