#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        row = [1]  # Start the row with [1]
        
        # Fill in the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        row.append(1)  # End the row with [1]
        
        triangle.append(row)  # Add the row to the triangle
    
    return triangle
