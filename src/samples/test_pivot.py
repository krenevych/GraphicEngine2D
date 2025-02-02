import numpy as np

from src.engine.Polygon import Polygon
from src.engine.Scene import Scene

if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_scene(self):
            triangle = Polygon()

            # Задаємо геометрію - пара послідовних значень визначає вершину на площині
            triangle.set_geometry(
                0, 0,
                2, 0,
                1, 1,
            )

            triangle.pivot(1, 0)
            triangle.show_pivot()
            triangle.show_local_frame()

            # Задаємо параметри полігону
            # triangle["show_frames"] = True
            triangle["color"] = "blue"         # колір ліній
            triangle["line_style"] = "--"      # стиль ліній
            # triangle["vertices_show"] = True   # показувати вершини
            # triangle["vertex_color"] = "grey"  # колір вершин
            # triangle["labels"] = [             # підписи верших зі зміщеннями
            #     (r'$P_1$', (-0.2, -0.6)),
            #     (r'$P_2$', (0.2, -0.2)),
            #     (r'$P_3$', (-0.1, 0.2)),
            #     # (r"$P_4$", (-0.2, 0.3)),
            #     # (r"$P_5$",(-0.7, -0.2)),
            # ]

            triangle.draw()

            # задаємо трансформацію
            # triangle.scale(2, 1)          # масштабування
            triangle.rotation(np.radians(30))    # поворот
            # triangle.translation(2, 1)    # перенесення
            triangle["line_style"] = "-"      # стиль ліній
            # малюємо полігон
            triangle.draw()


    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 3, 3),  #  розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,   #  чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,    # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  #  стиль ліній осей координат
    ).prepare()
    scene.draw_figures()
    scene.finalize()
