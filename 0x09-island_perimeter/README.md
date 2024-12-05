Key Points:

    The grid is rectangular and the maximum dimensions are 100x100.
    A cell has four potential edges (left, right, top, bottom), but only those touching water or the grid's boundary contribute to the perimeter.
    We should check each land cell (1):
        If the cell has a neighbor that is water (0) or is at the edge of the grid, then that edge contributes to the perimeter.

Plan:

    Iterate over each cell in the grid.
    For each 1 (land):
        Check the four directions (left, right, up, down).
        If a direction is out of bounds or contains 0 (water), it contributes to the perimeter.
    Sum the perimeter contributions and return the total.


