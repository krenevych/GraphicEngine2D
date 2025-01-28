from src.base.scene import Scene
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3

if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_scene(self):
            rect = SimplePolygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            rect.color = "grey"
            rect.line_style = ":"
            rect.draw()

            S = Mat3x3.scale(1, 3)
            print("=== Scale (from Mat3x3) ====")
            print(S)

            R = Mat3x3.rotation(60, is_radians=False)
            print("=== Rotation ====")
            print(R)

            T = Mat3x3.translation(2, 3)
            print("=== Translation ====")
            print(T)

            TRS = T * R * S
            print("=== Transform ====")
            print(TRS)

            rect.transformation = TRS
            rect.color = "red"
            rect.line_style = "-"
            rect.draw()

            RST = R * S * T
            rect.transformation = RST
            rect.color = "blue"
            rect.line_style = "-"
            rect.draw()


    SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-10, -10, 10, 10),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    ).draw()
