#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened or not
    Args:
      boxes: a list of lists
    """
    # List to hold the boolean result of every
    # individual box after conditional check
    # If the key of a box is found in another box, True otherwise
    # False is returned
    result = []
    for i in range(0, len(boxes) - 1):
        individual_box_result = []
        for box in boxes:
            if (i not in boxes[i]) and (i in box):
                individual_box_result.append(True)
            else:
                individual_box_result.append(False)
        individual_box_result = any(individual_box_result)
        result.append(individual_box_result)
    result.pop(0)
    result.insert(0, True)
    return all(result)
