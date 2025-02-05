import os

import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")
# Шлях до папки із зображеннями
image_folder = "/Users/andrii/repo/ComputerGraphics/GraphicEngine2D/images"

# Завантаження всіх зображень
images = [Image.open(os.path.join(image_folder, img)) for img in sorted(os.listdir(image_folder)) if
          img.endswith(('.png', '.jpg'))]

# Створення фігури
fig, ax = plt.subplots()
ax.axis('off')  # Прибрати осі

# Відображення першого зображення
img_plot = ax.imshow(images[0])


# Функція для оновлення кадру
def update(frame):
    img_plot.set_array(images[frame])
    return img_plot,


# Створення анімації
ani = FuncAnimation(fig, update, frames=len(images), interval=500, blit=True)

# Відображення анімації
plt.show()
