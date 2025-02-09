from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.SimplePolygon import SimplePolygon
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Mat4x4 import Mat4x4
from src.math.Vec4 import vertex

FIGURE_KEY = "rect"


class AnimatedSceneSample(AnimatedScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        polygon = SimplePolygon(self.plt_axis,  # створюємо полігон з заданою геометрією
            0, 2, 0,
            2, 0, 0,
            4, 2, 0,
            2, 4, 0,
        )
        polygon.show_local_frame()  # відмальовувати локальну систему координат
        polygon.set_local_frame_parameters(
            line_style="-.",
            color=("brown", "orange", "yellow"),
            line_width=1
        )
        # polygon.pivot(2, 2, 0)  # задати координати опорної точки
        polygon.show_pivot()  # відмальовувати опорну точку

        self[FIGURE_KEY] = polygon  # додати полігон з ключем "rect" на сцену


if __name__ == '__main__':
    animated_scene = AnimatedSceneSample(
        image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
        coordinate_rect=(-1, -1, -1, 6, 6, 6),  # розмірність системи координат
        title="Animated scene",  # заголовок рисунка
        grid_show=False,  # чи показувати координатну сітку
        base_axis_show=False,  # чи показувати базові осі зображення
        axis_show=True,  # чи показувати осі координат
        axis_color=("red", "green", "blue"),  # колір осей координат
        axis_line_width=2.0,  # товщина осей координат
        axis_line_style="--",  # стиль ліній осей координат
    ).prepare()

    def frame1(scene):
        fig = scene[FIGURE_KEY]
        fig.set_transformation(Mat4x4.translation(1, 1, 0))

    animated_scene.add_frames(frame1)

    translation = TranslationAnimation(  # створюємо анімацію переміщення
        end=vertex(1, 1, 0),  # значення точки у яку треба перемітити
        channel=FIGURE_KEY,  # ідентифікатор фігури до якої має застосовуватися анімація
        frames=120,  # кількість кадрів анімації
    )
    #
    # translation2 = TranslationAnimation(
    #     end=vertex(0, 0),
    #     channel=FIGURE_KEY,
    #     frames=20,
    # )
    #
    # scale_before = ScaleAnimation(
    #     end=(1.2, 1.2, 1.2),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )
    #
    # scale_before2 = ScaleAnimation(
    #     end=(1, 1, 1),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )

    scale = ScaleAnimation(
        end=(1.5, 1.5, 1.5),
        frames=120,
        channel=FIGURE_KEY,
        apply_geometry_transformation_on_finish=True,
    )
    #
    # scale2 = ScaleAnimation(
    #     end=(0.5, 0.5, 0.5),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )
    #
    # scale3 = ScaleAnimation(
    #     end=(1, 1, 1),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )
    #
    # rotation = RotationAnimation(
    #     end=np.radians(30),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )
    #
    # rotation2 = RotationAnimation(
    #     end=np.radians(-30),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )
    #
    # rotation3 = RotationAnimation(
    #     end=np.radians(0),
    #     frames=20,
    #     channel=FIGURE_KEY,
    # )

    # задаємо послідовність анімацій
    # animated_scene.add_animation(scale_before)
    # animated_scene.add_animation(scale_before2)
    animated_scene.add_animation(scale)
    # animated_scene.add_animation(rotation)
    animated_scene.add_animation(translation)
    # animated_scene.add_animation(scale2)
    # animated_scene.add_animation(translation2)
    # animated_scene.add_animation(rotation2)
    # animated_scene.add_animation(scale3)
    # animated_scene.add_animation(rotation3)
    animated_scene.animate()


    # animated_scene.draw()
    # animated_scene.finalize()
