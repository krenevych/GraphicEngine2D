from matplotlib.patches import Polygon
import matplotlib.pyplot as plt


def draw_poly(vertices,
              facecolor='green', edgecolor='black', linewidth=2):
    # Створення багатокутника
    polygon = Polygon(vertices, closed=True, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth)

    # Створення графіка
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.add_patch(polygon)

    # Налаштування меж графіка
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal', adjustable='box')

    # Підписи та відображення
    plt.title("Багатокутник із Polygon")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # Координати вершин багатокутника
    vertices = [(1, 1), (3, 1), (4, 3), (2, 4)]
    draw_poly(vertices)
