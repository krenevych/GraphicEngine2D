from src.base.broken_line import draw_broken_line
from src.engine.model.Model import Model
from src.engine.scene.Scene import Scene


class BrokenLine(Model):

    def __init__(self, plt_axis,
                 *vertices,
                 color="black",
                 linewidth=1.0, linestyle="solid",
                 ):
        super().__init__(plt_axis, *vertices)

        self.color = color
        self.linestyle = linestyle
        self.linewidth = linewidth

    def draw_model(self):
        transformed_geometry = self.transformed_geometry
        ps = [el.xyz for el in transformed_geometry]

        draw_broken_line(
            self.plt_axis,
            ps,
            color=self.color,
            linewidth=self.linewidth,
            linestyle=self.linestyle
        )


if __name__ == '__main__':
    MODEL_KEY = "model"


    class LineScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            vector = BrokenLine(self.plt_axis,
                                0, 0, 0,
                                0.557, 0.500, 0.663,
                                1, 1, 1,
                                -1, 1, 1,
                                0, 0, 0,
                                )
            self[MODEL_KEY] = vector
            vector.color = "brown"


    ##############################################
    ##############################################

    ############## Frame 1 ##################
    def frame1(scene: Scene):
        vector: BrokenLine = scene[MODEL_KEY]
        print("initial geom")
        print(vector.transformed_geometry[1].xyz)


    simple_scene = LineScene(
        image_size=(8, 8),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 1, 1, 1),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        # axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    simple_scene.add_frames(
        frame1,
    )  # додаємо кадри на сцену

    simple_scene.draw()
    simple_scene.finalize()
