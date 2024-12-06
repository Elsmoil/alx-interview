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
    boxes (list of list): List of boxes, each containing keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    # Number of boxes
    n = len(boxes)

    # A list to track which boxes have been unlocked
    unlocked = [False] * n

    # The first box is always unlocked
    unlocked[0] = True

    # A list to store keys we have found and can use to open other boxes
    keys_to_check = [0]

    # Start exploring the boxes
    while keys_to_check:
        current_box = keys_to_check.pop()

        # Try to unlock boxes using keys found in the current box
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                # Add the box to the list of keys to check
                keys_to_check.append(key)

    # If all boxes are unlocked, return True; otherwise, False
    return all(unlocked)


# Test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
