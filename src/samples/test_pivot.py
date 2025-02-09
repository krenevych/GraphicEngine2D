import numpy as np

from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene
from src.math.Mat4x4 import Mat4x4

if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_frames(self):
            triangle = SimplePolygon(self.plt_axis)

            # Задаємо геометрію - пара послідовних значень визначає вершину на площині
            triangle.set_geometry(
                0, 1, 0,
                2, 1, 0,
                1, 2, 0,
            )
            triangle.color = "grey"


            triangle.pivot(1, 0, 0)
            triangle.show_pivot()
            triangle.show_local_frame()


            triangle.draw()

            # задаємо трансформацію
            triangle.set_transformation(Mat4x4.rotation_z(np.radians(30)))  # поворот
            triangle.draw()


    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 3, 3, 3),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()
    scene.draw()
    scene.finalize()
