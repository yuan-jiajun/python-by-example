"""
================================================================================
File: 01_test_basics.py
Topic: Introduction to Unit Testing with pytest
================================================================================

This file introduces unit testing, a professional practice used to ensure that 
code behaves as expected. We use 'pytest', the industry standard for Python.

Key Concepts:
- Writing test functions (starting with test_)
- Assertions (checking if conditions are True)
- Running tests from the terminal
================================================================================
"""

import pytest

# A simple function we want to test
def add(a: int, b: int) -> int:
    return a + b

def test_add_positive():
    """Test addition of positive numbers."""
    assert add(2, 3) == 5

def test_add_negative():
    """Test addition of negative numbers."""
    assert add(-1, -1) == -2

def test_add_zero():
    """Test addition with zero."""
    assert add(5, 0) == 5

if __name__ == "__main__":
    print("Run this file using: pytest 11_testing/01_test_basics.py")
