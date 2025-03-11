from src.engine.model.Model import Model
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene


class Cube(Model):

    def __init__(self, plt_axis):
        super().__init__(plt_axis)
        self.polygons = []

        alpha = 0.3
        color = "cyan"
        edgze_color = "blue"

        # вершини куба
        vertices = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]

        # Грані куба
        faces = [[vertices[j] for j in [0, 1, 2, 3]],
                 [vertices[j] for j in [4, 5, 6, 7]],
                 [vertices[j] for j in [0, 1, 5, 4]],
                 [vertices[j] for j in [2, 3, 7, 6]],
                 [vertices[j] for j in [1, 2, 6, 5]],
                 [vertices[j] for j in [4, 7, 3, 0]]]

        for i, face in enumerate(faces):
            self.polygons.append(
                SimplePolygon(self.plt_axis,
                              *face,
                              color=color,
                              edgecolor=edgze_color,
                              alpha=alpha,
                              ))

    def draw_model(self):
        for polygon in self.polygons:
            polygon.transformation = self.transformation
            polygon.draw()


if __name__ == '__main__':
    CUBE_KEY = "cube"


    class CubeScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            cube = Cube(self.plt_axis)
            self[CUBE_KEY] = cube
            cube.show_pivot()
            cube.show_local_frame()


    ############## Frame 1 ##################
    def frame1(scene: Scene):
        cube: SimplePolygon = scene[CUBE_KEY]


    simple_scene = CubeScene(
        image_size=(8, 8),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 1, 1, 1),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    simple_scene.add_frames(
        frame1,
    )  # додаємо кадри на сцену

    simple_scene.draw()
    simple_scene.finalize()
