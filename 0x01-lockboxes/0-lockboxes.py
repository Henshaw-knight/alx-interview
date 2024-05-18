#!/usr/bin/python3
def canUnlockAll(boxes):
    # List to hold the boolean result of every
    # individual box after conditional check
    # If the key of a box is found in another box, True otherwise
    # False is returned
    result = []
    for i in range(1, len(boxes) - 1):
        # start from box with index 1, because 0 is always unlocked
        individual_box_result = []
        for box in boxes:
            if (i not in boxes[i]) and (i in box):
                individual_box_result.append(True)
            else:
                individual_box_result.append(False)
        individual_box_result = any(individual_box_result)
        result.append(individual_box_result)
    return all(result)
