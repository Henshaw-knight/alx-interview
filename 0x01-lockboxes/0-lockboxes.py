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
            # Remove the key that can unlock the box holding it
            # to aid the checking
            if i in boxes[i]:
                boxes[i].remove(i)
            if (i in box):
                individual_box_result.append(True)
            else:
                individual_box_result.append(False)
        individual_box_result = any(individual_box_result)
        # for i == 0, True is appended because boxes[0] is always unlocked
        result.append(individual_box_result) if i != 0 else result.append(True)
    return all(result)
