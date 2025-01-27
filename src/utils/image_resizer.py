import os
from PIL import Image


def resize_images_in_folder(folder_path, output_folder=None):
    """
    Зменшує розмір усіх зображень у папці вдвічі.

    :param folder_path: Шлях до папки з вхідними зображеннями.
    :param output_folder: Шлях до папки для збереження зменшених зображень. Якщо None, замінює оригінали.
    """
    # Перевіряємо існування папки
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не існує.")
        return

    # Створення вихідної папки, якщо потрібно
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Перебір усіх файлів у папці
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Перевірка, чи є файл зображенням
        try:
            with Image.open(file_path) as img:
                # Зменшення розміру
                new_size = (img.width // 2, img.height // 2)
                resized_img = img.resize(new_size)

                # Збереження зображення
                save_path = os.path.join(output_folder, filename) if output_folder else file_path
                resized_img.save(save_path)
                print(f"Зображення {filename} зменшено та збережено у {save_path}")
        except Exception as e:
            print(f"Пропуск {filename}: {e}")


# Використання
folder = "/Users/andrii/repo/ComputerGraphics/GraphicEngine2D/images"  # Замініть на шлях до вашої папки
output_folder = f"{folder}/output"  # Замініть на вихідну папку або None, щоб замінити оригінали
resize_images_in_folder(folder, output_folder)
