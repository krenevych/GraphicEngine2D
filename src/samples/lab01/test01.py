from src.engine.Scene import Scene
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3


if __name__ == '__main__':
    class SampleScene(Scene):
        def draw_figures(self):
            rect = SimplePolygon(
                0, 0,
                1, 0,
                1, 1,
                0, 1
            )
            rect.color = "blue"
            rect.line_style = "-"
            rect.draw()

            R_30 = Mat3x3.rotation(30, is_radians=False)
            T_2_3 = Mat3x3.translation(2, 3)
            T = T_2_3 * R_30
            T1 = R_30 * T_2_3

            print("=== Rotation ====")
            print(R_30)
            print("=== Translation ====")
            print(T_2_3)
            print("=== Transformation T * R ====")
            print(T)
            print("=== Transformation R * T ====")
            print(T1)

            # rect.transformation = T_2_3
            rect.transformation = R_30
            rect.color = "orange"
            rect.line_style = "-"
            rect.draw()

            # rect.transformation = R_30 * T_2_3
            rect.transformation = T_2_3 * R_30
            rect.draw()

    scene = SampleScene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    ).prepare()
    scene.draw_figures()
    scene.finalize()
