import numpy as np
from matplotlib.path import Path
import os

def point_in_polygon(point, poly):
    path = Path(poly.get_xy())
    return path.contains_point(point)

def calculate_area_irregular(points, poly, square_size):
    inside_points = np.array([point for point in points if point_in_polygon(point, poly)])
    area_square = square_size ** 2
    area_irregular_estimated = (len(inside_points) / len(points)) * area_square
    return area_irregular_estimated, inside_points

def save_irregular_points(filename):
    # Define the irregular figure's points
    irregular_points = np.array([
        [2, 2], [4, 1], [6, 2], [7, 5], [5, 8], [2, 6]
    ])

    if os.path.exists(filename):
        os.remove(filename)

    # Save the points to a .npy file
    np.save(filename, irregular_points)
