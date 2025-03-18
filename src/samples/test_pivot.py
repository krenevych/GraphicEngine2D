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
        coordinate_rect=(-1, -1, -1, 3, 3, 3),  # розмірність системи координат
        axis_line_style="-."  # стиль ліній осей координат
    )
    scene.show()
