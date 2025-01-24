from src.base.scene import draw_scene
from src.engine.drawer import line2d
from src.math.Vec3 import Vec3


def scene():
    """
    Головна функція, у якій опишіть всі обʼєкти, що мають відображатися на сцені
    """
    p1 = Vec3(0, 0, 1)  # Перша точка, третя координата 1 - вказує, що саме точка у двовиміному просторі
    p2 = Vec3(1, 0, 1)  # Друга точка
    p3 = Vec3(0, 1, 1)  # Третя точка

    labels = [                # Підписи точок
        (r'$p_1$', (-0.15, -0.2)),   # кортеж (імʼя, абсолютне зміщення)
        (r'$p_2$', (-0.05, 0.1)),    # абсолютне зміщення - необовʼязковий параметр
        (r'$p_3$', (0.05, 0.1)),
    ]

    line2d(p1, p2, p3,    # зображуємо лінію за трьома точками
           closed=True,          # лінія замкнена
           color="green",        # колір лінії
           line_style="--",      # стиль лінії
           vertex_color="grey",  # колір вершини
           labels=labels,        #  підписи
           labels_fontsize=16,   #  розмірр шрифтра
           labels_color="brown"  # колір надписів
           )



if __name__ == '__main__':
    draw_scene(
        scene=scene,       # функція у якій описується сцена
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, 2, 2),  #  розмірність системи координат
        title="Picture",  # заголовок рисунка
        grid_show=False,   #  чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,    # чи показувати осі координат
        axis_color="red",  # колір осей координат
        axis_line_style="-."  #  стиль ліній осей координат
    )
