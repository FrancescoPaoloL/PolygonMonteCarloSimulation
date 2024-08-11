import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

def plot_figure(square_size, irregular_polygon, points, inside_points, area_irregular_estimated):
    fig, ax = plt.subplots()
    ax.set_xlim(0, square_size)
    ax.set_ylim(0, square_size)
    ax.set_aspect('equal')

    square = Rectangle((0, 0), square_size, square_size, fill=None, edgecolor='blue')
    ax.add_patch(square)
    ax.add_patch(irregular_polygon)

    ax.plot(points[:, 0], points[:, 1], 'b.', alpha=0.2, label='Points in Square', markersize=1)
    ax.plot(inside_points[:, 0], inside_points[:, 1], 'r.', label='Points in Irregular Figure', markersize=1)

    
    plt.legend()
    plt.title(f'Estimated Area of Irregular Figure: {area_irregular_estimated:.2f} square units')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    plt.text(1, square_size - 1, f'Square Side: {square_size}', fontsize=12, color='blue', ha='left')
    plt.text(1, square_size - 2, f'Square Area: {square_size ** 2}', fontsize=12, color='blue', ha='left')

    plt.show()
