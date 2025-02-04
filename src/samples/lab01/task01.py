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
            self["rect"] = rect
            rect.color = "blue"
            rect.line_style = ":"
            self.draw("rect")

            R_30 = Mat3x3.rotation(45, is_radians=False)

            rect.transformation = R_30
            rect.color = "orange"
            rect.line_style = ":"
            self.draw("rect")

            T_2_3 = Mat3x3.translation(2, 3)

            rect.transformation = T_2_3
            rect.color = "orange"
            rect.line_style = ":"
            self.draw("rect")

            # rect.transformation = R_30 * T_2_3
            rect.color = "red"
            rect.line_style = "-"
            rect.transformation = T_2_3 * R_30
            self.draw("rect")

            rect.transformation = R_30 * T_2_3
            self.draw("rect")


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
