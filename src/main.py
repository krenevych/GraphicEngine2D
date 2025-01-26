import numpy as np

from src.base.scene import draw_scene
from src.engine.Polygon import Polygon


def scene():
    m = Polygon()

    m.set_geometry(
        0, 0,
        2, 0,
        2, 1,
        1, 2,
        0, 1
    )


    m["closed"] = True
    m["color"] = "blue"
    m["line_style"] = "--"
    m["vertex_color"] = "grey"
    m["vertices_show"] = True
    m["labels"] = [
        (r'$P_1$', (-0.2, -0.6)),
        (r'$P_2$', (0.2, -0.2)),
        (r'$P_3$', (-0.1, 0.2)),
        (r"$P_4$", (-0.2, 0.3)),
        (r"$P_5$",(-0.7, -0.2)),
    ]

    m.scale(2, 1)
    m.translation(2, 1)
    m.rotation(np.radians(45))

    m.draw()


if __name__ == '__main__':
    draw_scene(
        scene=scene,       # функція у якій описується сцена
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 6, 6),  #  розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,   #  чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,    # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  #  стиль ліній осей координат
    )
