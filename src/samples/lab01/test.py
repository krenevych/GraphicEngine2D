from src.base.scene import draw_scene
from src.engine.simple.SimplePolygon import SimplePolygon
from src.math.Mat3x3 import Mat3x3


def scene():
    rect = SimplePolygon(
        2, 2,
        3, 2,
        3, 3,
        2, 3
    )
    rect.color = "blue"
    rect.line_style = ":"
    rect.draw()

    R = Mat3x3.rotation(65, is_radians=False)

    rect.transformation = R
    rect.draw()

if __name__ == '__main__':
    draw_scene(
        scene=scene,  # функція у якій описується сцена
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-3, -1, 6, 6),  # розмірність системи координат
        title="Picture",  # заголовок рисунка
        # grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green"),  # колір осей координат
        axis_line_style="-.",  # стиль ліній осей координат
        keep_aspect_ratio = True,
    )
