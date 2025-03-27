


from src.engine.model.Polygon import Polygon
from src.engine.scene.Scene import Scene
from src.math.Mat3x3 import Mat3x3
from tests.utils.image_utils import images_are_equal


def test_plot_image_output(tmp_path):
    ##################################################
    ##################################################

    FIGURE_KEY = "rect"

    T_P = Mat3x3.translation(-0.5, -0.5)
    T_P_inv = T_P.inverse()
    S = Mat3x3.scale(2, 3)

    def frame1(scene):
        rect = scene[FIGURE_KEY]

    def frame2(scene):
        rect = scene[FIGURE_KEY]
        rect.line_style = "solid"
        rect.color = "green"
        rect.transformation = T_P_inv * S * T_P  # повертаємо опорну точку на її місце

    scene = Scene(
        coordinate_rect=(-1, -2, 4, 4),  # розмірність системи координат
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio=True,
    )
    scene[FIGURE_KEY] = Polygon(
        0, 0,
        1, 0,
        1, 1,
        0, 1
    )
    scene[FIGURE_KEY].color = "blue"
    scene[FIGURE_KEY].line_style = ":"

    scene.add_frames(frame1,
                     frame2,
                     )

    ##################################################
    ##################################################

    output_file = tmp_path / "test_plot.png"
    scene.show(output_file)

    # Порівнюємо з еталонним
    assert images_are_equal(output_file, "expected/Figure_1.png")
