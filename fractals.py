import pygame
from tools import Block  # Импорт класса Block из модуля tools
import random  # Этот модуль пригодится нам для перемешивания координат


class Window:  # Создаем класс для поверхности рисования

    def __init__(self):  # Инициализация ообъекта: задаем атрибуты
        pygame.init()  # Инициализируем Pygame
        self._running = True  # атрибут работа цикла - True
        self._size = self.width, self.height = 640, 480  # Задаем длину и ширину окна
        self._display_surf_color = (0, 0, 0)  # Цвет заливки
        self._size_of_block = self.height_of_block, self.width_of_block = 10, 10  # Размеры блока
        self._direction_of_movement = 1  # Направление движения
        self._display_surf = pygame.display.set_mode(self._size)  # Создаем окно
        self._clock = pygame.time.Clock()  # Добавляем в инициализацию окна атрибут "таймер"

        self._color_of_block_standard = (155, 155, 200)  # Стандартный цвет блока
        self._color_of_block_current = (200, 155, 155)  # Цвет текщего блока
        self._color_of_block_was_find = (155, 200, 155)   # Цвет найденного блока

        self._lines = []  # Пустой список для линий
        self._depth = 6  # Глудина дерева
        self._h_line = None  # атрибут для горизонтальной линии (мы заполним его в методе создания),
        self._v1_line = None  # для первой вертикальной линии
        self._v2_line = None  # для второй вертикальной линии
        self._length_of_line = 200  # Длина линии
        self._x_of_line = self.width / 2  # Координаты центра - половина ширины окна
        self._y_of_line = self.height / 2  # и половина высоты окна

    @staticmethod  # Эта метка говорит о том, что метод статический. Он не изменяет никакие объекты,
    # а работает только с параметрами, которые в него передали.
    def on_cleanup():  # Метод завершения программы
        pygame.quit()

    # Создаем метод для изменения атрибутов у объектов-атрибутов, которые были созданы при инициализации
    def on_init(self):
        self._display_surf.fill(self._display_surf_color)  # Заполняем окно цветом

    def h_tree(self, depth, length, x, y):

        if depth != 0:  # Проверяем не пора ли остановиться
            x0 = x - length / 2  # Вычисляем
            x1 = x + length / 2  # нужные
            y0 = y - length / 2  # координаты
            y1 = y + length / 2

            self._h_line = Block(size=(length, 2), color=self._color_of_block_standard)  # Создаем
            self._v1_line = Block(size=(2, length), color=self._color_of_block_standard)  # для
            self._v2_line = Block(size=(2, length), color=self._color_of_block_standard)  # каждой линии

            # Задаем нужные координаты
            self._h_line.set_x(x0)
            self._h_line.set_y(y)

            self._v1_line.set_x(x0)
            self._v1_line.set_y(y0)

            self._v2_line.set_x(x1)
            self._v2_line.set_y(y0)

            # Добавляем линии в список
            self._lines.append(self._h_line)
            self._lines.append(self._v1_line)
            self._lines.append(self._v2_line)

            self.h_tree(depth - 1, length / 2, x0, y0)  # Рекурсивный
            self.h_tree(depth - 1, length / 2, x0, y1)  # вызов
            self.h_tree(depth - 1, length / 2, x1, y0)  # функции
            self.h_tree(depth - 1, length / 2, x1, y1)  # на концах линий

    def on_loop(self):  # В цикле
        self.h_tree(self._depth, self._length_of_line, self._x_of_line, self._y_of_line)

    def on_event(self, event):  # Метод обработка событий
        if event.type == pygame.QUIT:
            self._running = False

    def on_render(self):  # Метод вывода на экран
        self._display_surf.fill(self._display_surf_color)  # Если требуется обновляем заливку
        for line in self._lines:  # С помощью цикла
            self._display_surf.blit(line.image, line.rect)  # Рисуем линии
        pygame.display.flip()  # Обновление

    def on_start(self):  # Метод запуск основного цикла
        self.on_init()  # Вызов изменения атрибутов
        while self._running:  # Проверяем атрибут "работа цикла"
            self._clock.tick(60)  # Вызываем метод tick()
            for event in pygame.event.get():
                self.on_event(event)  # Вызываем обработчик событий
            self.on_loop()  # Движение блока
            self.on_render()  # Вызываем перерисовку
        self.on_cleanup()  # Завершение программы происходит после выхода из основного цикла


window = Window()
window.on_start()