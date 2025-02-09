from src.base.axes import draw_axis
from src.engine.model.BaseModel import BaseModel
from src.engine.scene.Scene import Scene


class Vector(BaseModel):

    def __init__(self, plt_axis, *vertices):
        super().__init__(plt_axis, *vertices)

        self.linestyle = "-."
        self.linewidth = 1.0

    def draw_model(self):
        transformed_geometry = self.transformed_geometry
        ps = [el.xyz for el in transformed_geometry]

        draw_axis(
            self.plt_axis,
            ps[0], ps[1],
            color=self.color,
            linewidth=self.linewidth,
            linestyle=self.linestyle
        )


if __name__ == '__main__':
    VECT_KEY = "rect"


    class VectorScene(Scene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            vector = Vector(self.plt_axis,
                            0, 0, 0,
                            0.557, 0.500, 0.663
                            )
            self[VECT_KEY] = vector
            vector.color = "brown"

            # vector.show_pivot()
            # vector.show_local_frame()


    ##############################################
    ##############################################

    ############## Frame 1 ##################
    def frame1(scene: Scene):
        vector: Vector = scene[VECT_KEY]
        print("initial geom")
        print(vector.transformed_geometry[1].xyz)


    simple_scene = VectorScene(
        image_size=(8, 8),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 2, 2, 2),  # розмірність системи координатps
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
