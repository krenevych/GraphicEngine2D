import matplotlib

from src.engine.scene.Scene import Scene

matplotlib.use("TkAgg")

if __name__ == '__main__':
    FIGURE_KEY = "polygon"

    scene = Scene(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 3, 3, 3),  # розмірність системи координат
        title="3D система координат",  # заголовок рисунка
        # base_axis_show=True,  # чи показувати базові осі зображення
        grid_show=True,  # чи показувати координатну сітку
        # axis_show=False,  # чи показувати осі координат
        # axis_color=("red", "green", "blue"),  # колір осей координат
        axis_line_width=1.0,
        axis_line_style="--",  # стиль ліній осей координат
        axis_show_from_origin=True,
    )

    scene.prepare()  # налаштовує та зображує базові елементи сцени (розмірність, глобальна система координат, тощо.)
    # scene.add_frames(frame1)
    scene.draw()
    scene.finalize()
