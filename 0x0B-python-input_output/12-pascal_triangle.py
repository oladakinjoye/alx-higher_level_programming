#!/usr/bin/python3
"""Define a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmpp = [1]
        for i in range(len(tri) - 1):
            tmpp.append(tri[i] + tri[i + 1])
        tmpp.append(1)
        triangles.append(tmpp)
    return triangles
