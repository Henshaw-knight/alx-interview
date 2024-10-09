## Lockboxes challenge

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

### Task

Write a method that determines if **all the boxes can be opened**.

### Function Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
    boxes (list of lists): A list where each index represents a box and the list at each index contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, else False.
    """

