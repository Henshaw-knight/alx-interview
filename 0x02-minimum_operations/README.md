# Minimum Operations to Achieve n Characters

## Project Overview

This project focuses on devising an efficient solution to calculate the minimum number of operations required to achieve exactly **n** characters in a text file using only two operations:

- **Copy All**: Copies the entire content of the text file.
- **Paste**: Pastes the last copied content.

In a text file, there is a single character H. The text editor can execute only two operations in this file: Copy All and Paste. Given a number **n**, write a method that calculates the fewest number of operations needed to result in exactly **n** H characters in the file.

## Algorithm

The solution must efficiently compute the minimum number of operations needed by utilizing fundamental algorithmic and mathematical principles. It is important to understand that achieving **n** characters in the file can be broken down into a series of copy-paste operations, and this problem can be viewed as one involving factors of **n**.

### Function Prototype

```python
def minOperations(n):
    """
    Calculates the minimum number of operations to achieve exactly n H characters
    using only 'Copy All' and 'Paste' operations.

    Parameters:
    n (int): The target number of H characters.

    Returns:
    int: The fewest number of operations needed to reach n characters. 
         Returns 0 if n is impossible to achieve.
    """
```

### Example usage

```python
print(minOperations(9))   # Output: 6
print(minOperations(15))  # Output: 8
print(minOperations(1))   # Output: 0
```

### Detailed Example

For n = 9, the operations would be:
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
