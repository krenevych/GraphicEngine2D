from src.base.scene import draw_scene
from src.engine.drawer import line2d
from src.math.Vec3 import Vec3


def scene():
    """
    Головна функція, у якій опишіть всі обʼєкти, що мають відображатися на сцені
    """
    p1 = Vec3(0, 0, 1)
    p2 = Vec3(1, 0, 1)
    p3 = Vec3(0, 1, 1)

    labels = [
        (r'$p_1$', (-0.15, -0.2)),
        (r'$p_2$', (-0.05, 0.1)),
        (r'$p_3$', (0.05, 0.1)),
    ]

    line2d(p1, p2, p3,
           closed=True,
           color="green", vertex_color="yellow",
           labels=labels, line_style="--", labels_fontsize=16, labels_color="brown")


if __name__ == '__main__':
    draw_scene(
        scene=scene,       # функція у якій описується сцена
        coordinate_rect=(-1, -1, 2, 2),  #  розмірність системи координат
        grid_show=False,   #  чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,    # чи показувати осі координат
        axis_color="red",  # колір осей координат
        axis_line_style="-."  #  стиль ліній осей координат
    )
