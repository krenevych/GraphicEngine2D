from src.engine.model.Model import Model
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.Scene import Scene


class Cube(Model):

    def __init__(self,
                 plt_axis,
                 alpha=1.0,
                 color="cyan",
                 edge_color="blue",
                 line_style="-",
                 line_width=1.0,
                 ):
        super().__init__(plt_axis)
        self.polygons = []

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
        faces = [
            [vertices[j] for j in [0, 1, 2, 3]],
            [vertices[j] for j in [4, 5, 6, 7]],
            [vertices[j] for j in [0, 1, 5, 4]],
            [vertices[j] for j in [2, 3, 7, 6]],
            [vertices[j] for j in [1, 2, 6, 5]],
            [vertices[j] for j in [4, 7, 3, 0]]
        ]

        for i, face in enumerate(faces):
            self.polygons.append(
                SimplePolygon(self.plt_axis,
                              *face,
                              color=color,
                              edgecolor=edge_color,
                              alpha=alpha,
                              line_width=line_width,
                              line_style=line_style,
                              ))

    def draw_model(self):
        for polygon in self.polygons:
            polygon.transformation = self.transformation
            polygon.draw()

    def apply_transformation_to_geometry(self):
        super().apply_transformation_to_geometry()

        for polygon in self.polygons:
            polygon.apply_transformation_to_geometry()


if __name__ == '__main__':
    CUBE_KEY = "cube"


    class CubeScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            cube = Cube(self.plt_axis, alpha=0.1)
            self[CUBE_KEY] = cube
            cube.show_pivot()
            cube.show_local_frame()


    simple_scene = CubeScene(
        axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    )

    simple_scene.show()