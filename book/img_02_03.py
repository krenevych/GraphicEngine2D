import matplotlib.pyplot as plt
import numpy as np

from book.utils import calc_normal, drawVector, drawLength, drawPoint

FONT_SIZE = 20



def drawLineWithLength(p, u, ax,
                       color_vector="black",
                       caption="", color_caption="black", caption_normal_offset=0.1):

    drawVector(p, u,
               color_vector=color_vector,
               caption= "",caption_color="yellow" ,caption_normal_offset=caption_normal_offset
               )

    # Початок і кінець лінії
    start = p
    end = p + u

    perpendicular = calc_normal(u)
    delta = perpendicular * 0.03
    start, end = start + delta, end + delta

    drawLength(start, end, color_caption=color_caption, caption=caption, caption_normal_offset=caption_normal_offset)




if __name__ == '__main__':
    # Створення графіка
    fig, ax = plt.subplots(figsize=(6, 6))

    p = np.array([0.2, .3])
    u = np.array([0.6, 0.4])

    drawLineWithLength(p, u, ax, color_vector="red", caption=r'$\alpha v$', caption_normal_offset=0.06)

    p1 = np.array([0.6, 0.3])
    u1 = 0.3 * u

    drawLineWithLength(p1, u1, ax, color_vector="blue", caption=r'$v$', caption_normal_offset=0.05)

    p1 = np.array([0.2, .1])
    u1 = np.array([0.6, 0.4]) * 0.4
    drawVector(p1, u1, color_vector="green", caption=r"$T$", caption_color="red", caption_normal_offset=-0.05)

    # plt.plot(p[0], p[1], 'ko', label='P') // точку малює
    drawPoint(p1, size=100, color="blue", caption=r"$R$", color_caption="blue", offset=(-0.02, 0.05))
    # drawPoint(p1+u1, size=100, color="blue", caption=r"$R$", color_caption="blue", offset=(-0.02, 0.05))

    # Налаштування меж графіка
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title("Лінія з перпендикулярами на кінцях")
    plt.show()
