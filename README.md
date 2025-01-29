# GraphicEngine2D

**GraphicEngine2D** — це бібліотека для створення 2D графіки з використанням мови програмування Python.

## Можливості

- Зображення векторів та відрізків на площині.
- Зображення точок на площині.
- Зображення полігонів.
- Налаштування відображення фігур, що зображуються (кольори, товщина та стиль ліній тощо).
- Трансформації двовимірних обʼєктів (розтяг, обертання, перенесення).
- Анімації з використанням трансформацій

![Малюнок 1](images/img1.png)
![Малюнок 1](images/img2.png)
![Малюнок 1](images/img3.png)
![Малюнок 1](images/img6.png)
![Малюнок 1](images/img4.png)
![Малюнок 1](images/img5.png)

## Встановлення

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/krenevych/GraphicEngine2D.git
   cd GraphicEngine2D
   ```
2. Відкрийте репозиторій будь-якою IDE (проект створювався у Pycharm).
3. Встановіть додаткові модулі для роботи з математичними бібліотеками та бібліотеками візуалізації
   ```bash
   pip install numpy scipy matplotlib
   ```
4. Запустіть файл main.py на виконання, щоб переконатися, що середовище налаштоване правильно.

## Використання

1. Файл main.py містить приклад використання рушія.
2. Опишіть клас, що є нащадком класу
    - Scene для статичних зображень,
    - AnimatedScene для анімованих.
3. У цьому нащадку реалізуйте метод `draw_scene(self)`, у якому опишіть обʼєкти та їхнє розтащування (трансформації), що
   мають бути на сцені для статичного зображення.

```python

class SampleScene(Scene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ... # тут опишіть обʼєкти, та значення їхніх параметрів

    def draw_scene(self):
        ... # тут опишіть трансформацію обʼєктів та зміну значень їхніх параметрів

```

4. Для нащадку класу AnimatedScene додатково реалізуйте метод `on_frame(self, frame, start, end)`, що описує зображення
   сцени на кожному фреймі анімації [animated_scene.](src/samples/anim/animated_scene.py)

```python

class SampleScene(AnimatedScene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ...

    def draw_scene(self):
        ...

    def on_frame(self, frame, start, end):
        ...


```

5. У головній програмі створіть екземпляр описаної сцени

```python

scene = SampleScene(
    image_size=(5, 5),  # розмір зображення: 1 - 100 пікселів
    coordinate_rect=(-1, -1, 6, 6),  # розмірність системи координат
    title="Picture",  # заголовок рисунка
    grid_show=False,  # чи показувати координатну сітку
    base_axis_show=False,  # чи показувати базові осі зображення
    axis_show=True,  # чи показувати осі координат
    axis_color=("red", "green"),  # колір осей координат
    axis_line_style="-."  # стиль ліній осей координат
)

```

- coordinate_rect: Розмір системи координат у форматі (x_min, y_min, x_max, y_max).
- grid_show: Увімкнення/вимкнення сітки (булеве значення).
- base_axis_show: Увімкнення/вимкнення базових осей (булеве значення).
- axis_show: Увімкнення/вимкнення осей координат.
- axis_color: Колір осей (наприклад, "red", "blue" тощо).
- axis_line_style: Стиль ліній осей (наприклад, "-", "--", "-." тощо).


6. та відобразіть її методом `draw()`:

```python
scene.draw()  # відобразити сцену на екрані
```

7. Для анімованої сцени використайте метод `animate()` у якому задайте параметри початкового та кінцевого значення
   трансформації, кількість та частоту кадрів, чи повторювати анімацію циклічно та задайте спостерігача для нотифікації про події анімації

```python

scene.animate(start=vertex(0, 0),
              end=vertex(2, 2),
              repeat=True,
              animation_listener)

```

- start - початкове значення трансформації
- end - кінцеве значення трансформації
- repeat - чи повторювати анімацію циклічно - значення за промовчанням `False`
- frame - кількість кадрів анімації - значення за промовчанням `100`
- interval - час в мілісекундах між кадрами анімації - значення за промовчанням `16`, що відповідає `1/60` секунди (FPS=60)
- animation_listener - екземпляр нащадку класу `AnimationListener` - спостерігач, що реагує на зміни стану анімації

```python

class AnimListenerAllEvent(AnimationListener):

    def on_start(self):  # реація на початок анімації
        print("Started animation")

    def on_repeat(self):  # реакція на початок наступного циклу анімації, при циклічній анімації
        print("Animation repeat")

    def on_finish(self):  # реакція на завершення анімації
        print("Finished animation")


animation_listener = AnimListenerAllEvent()

```