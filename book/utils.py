import numpy as np
import matplotlib.pyplot as plt

FONT_SIZE = 20

def calc_normal(start, end=None):
    if end == None:
        direction = start
        direction = direction / np.linalg.norm(direction)  # Нормалізація вектора

        # Обчислення перпендикулярного вектора
        __perpendicular = np.array([-direction[1], direction[0]])
        return __perpendicular
    else:
        # Вектор напряму лінії
        direction = end - start
        return calc_normal(direction)

def drawVector(p, u,
               color_vector="black",
               caption="", caption_color="black", fontsize=FONT_SIZE, caption_normal_offset=0.1):
    # малювання вектора
    plt.quiver(p[0], p[1], u[0], u[1], angles='xy', scale_units='xy', scale=1, color=color_vector, label='First Set')
    # plt.arrow(p[0], p[1], u[0], u[1],color=color_vector, head_width=0.03, length_includes_head=True, label=r'$\alpha_2 v_2$')


    if caption is not None and caption != "":
        perpendicular = calc_normal(u)
        delta_text = perpendicular * caption_normal_offset
        v2 = p + u * 0.5 + delta_text
        plt.text(float(v2[0]), float(v2[1]), caption, fontsize=fontsize, color=caption_color, ha='left')


def drawLength(start, end, color_line="black", linestyle="--",
               caption="", color_caption="black", fontsize=FONT_SIZE, caption_normal_offset=0.1):

    # Малювання лінії довжини
    plt.plot([start[0], end[0]], [start[1], end[1]], color=color_line, linestyle=linestyle, linewidth=1.4)

    # Малювання перпендикулярних ліній на кінцях
    # Довжина перпендикулярних ліній
    length = 0.05
    perpendicular = calc_normal(end-start)
    # Для початкової точки
    perp_start = start + length * perpendicular
    perp_end = start - length * perpendicular
    plt.plot([perp_start[0], perp_end[0]], [perp_start[1], perp_end[1]], color=color_line, linewidth=1.4)

    # Для кінцевої точки
    perp_start = end + length * perpendicular
    perp_end = end - length * perpendicular
    plt.plot([perp_start[0], perp_end[0]], [perp_start[1], perp_end[1]], color=color_line, linewidth=1.4)

    if caption is not None and caption != "":
        delta_text = perpendicular * caption_normal_offset
        caption_pos = (start + end) * 0.5 + delta_text
        plt.text(float(caption_pos[0]), float(caption_pos[1]), caption, fontsize=fontsize, color=color_caption, ha='left')


def drawPoint(start, size = 50, color="black",
               caption="", color_caption="black", fontsize=FONT_SIZE, offset=(0, 0)):

    # plt.plot(start[0], start[1], "ko", label=caption, )
    plt.scatter(*start, color=color, label=caption, s=size)  # s - розмір точки

    if caption is not None and caption != "":
        caption_pos = start + offset
        plt.text(float(caption_pos[0]), float(caption_pos[1]), caption, fontsize=fontsize, color=color_caption, ha='left')


def draw_2d_poligon(*coords, ):
    for el in coords:
        assert len(el) == 2

    # plt.plot(coords, color=color_line, linestyle=linestyle, linewidth=1.4)

if __name__ == '__main__':
    pass