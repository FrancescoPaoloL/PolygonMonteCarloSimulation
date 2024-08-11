import numpy as np
from matplotlib.patches import Polygon
from geometry import calculate_area_irregular, save_irregular_points
from plotting import plot_figure

def get_irregular_points_file():
    return 'irregular_points.npy'

def main():
    filename = get_irregular_points_file()
    save_irregular_points(filename)

    irregular_points = np.load(filename)

    square_size = 10
    irregular_polygon = Polygon(irregular_points, closed=True, edgecolor='orange', facecolor='orange', alpha=0.5)

    num_points = 100000
    x = np.random.uniform(0, square_size, num_points)
    y = np.random.uniform(0, square_size, num_points)
    points = np.column_stack((x, y))

    area_irregular_estimated, inside_points = calculate_area_irregular(points, irregular_polygon, square_size)
    print(f'Estimated Area of Irregular Figure: {area_irregular_estimated:.2f} square units')

    plot_figure(square_size, irregular_polygon, points, inside_points, area_irregular_estimated)

if __name__ == '__main__':
    main()