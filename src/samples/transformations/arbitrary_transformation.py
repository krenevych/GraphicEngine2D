from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import Vec4, vertex

if __name__ == '__main__':
    RECT_KEY = "rect"
    O = vertex(0, 0, 0)
    t1 = Vec4(1, 0, 0)
    t2 = Vec4(1, 1, 0)
    t3 = Vec4(0, 1, 0)


    class SimplePolygonScene(AnimatedScene):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

            polygon = SimplePolygon(self.plt_axis,
                                    O,
                                    O + t1,
                                    O + t2,
                                    O + t3,
                                    edgecolor="red",
                                    )
            self[RECT_KEY] = polygon
            polygon.show_local_frame()
            print(polygon.transformed_geometry)


    animated_scene = SimplePolygonScene(
        image_size=(10, 10),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 2, 2, 2),  # розмірність системи координатps
        title="Picture",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        # axis_color="grey",  # колір осей координат
        axis_line_style="-."  # стиль ліній осей координат
    ).prepare()

    T = Mat4x4.translation(1, 1, 0)


    def frame1(scene):
        obj: SimplePolygon = scene[RECT_KEY]
        pass


    def frame2(scene):
        obj: SimplePolygon = scene[RECT_KEY]
        obj.set_transformation(T)


    animated_scene.add_frames(frame1, frame2)
    animated_scene.draw()
    animated_scene.finalize()
