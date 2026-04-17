# Python Code Review & Debugging

This project demonstrates the process of reviewing and improving Python code.

## Issues Identified

- The function incorrectly accumulates the index instead of the actual values
- No validation for empty lists (risk of division by zero)

## Improved Version

```python
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
