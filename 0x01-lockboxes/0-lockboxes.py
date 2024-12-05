#!/usr/bin/python3

"""
    This module contains the function `canUnlockAll`
    that determines if all boxes can be unlocked.
    Each box contains keys to other boxes,
    and the first box is unlocked initially.
    """


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of list of ints): A list of lists where each
        sublist represents the keys in a box.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    unlocked = set([0])  # We start by unlocking box 0
    keys_to_check = [0]  # Start with box 0

    while keys_to_check:
        current_box = keys_to_check.pop()  # Get the next box to process

        # Loop through the keys in the current box
        for key in boxes[current_box]:
            if key not in unlocked:
                unlocked.add(key)  # Add the key (box) to unlocked set
            # Add the new unlocked box to the list to check
            keys_to_check.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
