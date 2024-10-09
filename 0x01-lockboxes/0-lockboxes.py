#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened or not
    Args:
      boxes: a list of lists
    Returns:
      True if all boxes can be opened, else False is returned.
    """
    all_boxes = set()
    unique_keys = {0}
    for index, box in enumerate(boxes):
        all_boxes.add(index)
        for key in box:
            if key != index:
                unique_keys.add(key)
    return True if unique_keys == all_boxes else False
