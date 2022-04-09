import pygame
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

        self._height_for_find = 180  # Высота искомого блока
        self._next_block = 0  # Переменная счетчик
        self._go_to_find = True  # Переменная флаг продолжение "поиска"

        self._color_of_block_standard = (155, 155, 200)  # Стандартный цвет блока
        self._color_of_block_current = (200, 155, 155)  # Цвет текщего блока
        self._color_of_block_was_find = (155, 200, 155)  # Цвет найденного блока

        self._number_of_blocks = 20  # Количество элнментов в списке блоков
        self.blocks = []  # Пустой список
        self.xs_of_blocks = []  # Пустой список для перемешивания координат
        self.need_swap = False  # Флаг перестановки
        self.counter = 0  # Начало несортированного списка

        # Значения на первой итерации
        self._high_of_list = self._number_of_blocks - 1  # Большее значение = количество элементов - 1
        self._low_of_list = 0  # Меньшее значение = 0
        # Номер проверяемого элемента - целое цисло от середины
        self._middle_of_list = int((self._high_of_list + self._low_of_list) / 2)

    @staticmethod  # Эта метка говорит о том, что метод статический. Он не изменяет никакие объекты,
    # а работает только с параметрами, которые в него передали.
    def on_cleanup():  # Метод завершения программы
        pygame.quit()

    # Создаем метод для изменения атрибутов у объектов-атрибутов, которые были созданы при инициализации
    def on_init(self):
        self._display_surf.fill(self._display_surf_color)  # Заполняем окно цветом

        # Заполним список блоками. Количество итераций = количеству элементов в списке.
        for i in range(self._number_of_blocks):  # i - переменная итератор.
            temp_block = Block(size=(self.width_of_block, self.height_of_block + i * 10),  # Временный блок
                               color=self._color_of_block_standard)  # Высота растет на 10 с каждой итерацией
            temp_block.set_x(200 + i * 11)  # По X сдвигаем вправо каждый шаг
            temp_block.set_y(300 - i * 10)  # По Y сдвигаем вверх на 10 еаждый шаг
            self.blocks.append(temp_block)  # Добавляем блок к списку
            self.xs_of_blocks.append(temp_block.get_x())  # Добавляем координату X в список

            self.shuffle()  # перемешиваем блоки

    def shuffle(self):  # Метод перемешивание
        random.shuffle(self.xs_of_blocks)  # Функция "перемешивание списка" из модуля import
        for i, x in enumerate(self.xs_of_blocks):  # Создаем кортежи из порядкового номера и координаты
            self.blocks[i].set_x(x)  # Подставляем в блоки по порядку "перемешанные" координаты

    def on_loop(self):  # В цикле
        # Проверим первый элемент несортированного списка
        if self.counter <= len(self.blocks) - 2:  # Если он предпоследний или меньше
            # Сортируем
            self.need_swap = False  # Установим флаг необходимости перестановки в False
            min_of_x = self.blocks[self.counter].get_x()  # Задаем мин. значение - первое в несортированом списке
            index_of_min_x = self.counter  # Индексу минимального значения присвоим начало несортированного списка
            # Проход по всем элементам несортированной части списка
            for i, block in enumerate(self.blocФks[self.counter:], start=self.counter):
                if block.get_x() < min_of_x:  # Сравнение координаты X с минимальным значением
                    self.need_swap = True  # Если есть значение координаты меньше первого, то нужна перестановка
                    min_of_x = block.get_x()  # Меняем значение минимальной кординаты, т.к. найдено меньшее
                    index_of_min_x = i  # Запоминиаем индекс

            if self.need_swap:  # Если надо менять местами элементы
                # Присваиваем минимальному элементу координату первого
                self.blocks[index_of_min_x].set_x(self.blocks[self.counter].get_x())
                self.blocks[self.counter].set_x(min_of_x)  # Первому - минимальную координату

            # Для наглядности будем раскрашивать тот элемент, для которого будет идти поиск на следующей итерации
            # Элемент, который помтавили на место красим в стандартный
            self.blocks[self.counter].set_color(self._color_of_block_standard)
            self.counter += 1  # Сдвигаем границу сортировки на 1
            # И красим элемент для которго ищем место в текущий цвет
            self.blocks[self.counter].set_color(self._color_of_block_current)

    def on_event(self, event):  # Метод обработка событий
        if event.type == pygame.QUIT:
            self._running = False

    def on_render(self):  # Метод вывода на экран
        self._display_surf.fill(self._display_surf_color)  # Если требуется обновляем заливку
        for block in self.blocks:  # С помощью цикла
            self._display_surf.blit(block.image, block.rect)  # Выводим на экран блоки
        pygame.display.flip()  # Обновление

    def on_start(self):  # Метод запуск основного цикла
        self.on_init()  # Вызов изменения атрибутов
        while self._running:  # Проверяем атрибут "работа цикла"
            self._clock.tick(1)  # Вызываем метод tick()
            for event in pygame.event.get():
                self.on_event(event)  # Вызываем обработчик событий
            self.on_loop()  # Движение блока
            self.on_render()  # Вызываем перерисовку
        Window.on_cleanup()  # Завершение программы происходит после выхода из основного цикла


# Класс блока, который будет элементом в визуализациях будущих алгоритмах поиска и сортировки
class Block:

    def __init__(self, size=(0, 0), color=(0, 0, 0)):  # Атрибуты размер и цвет будут заданы при инициализации
        self.image = pygame.Surface(size)  # В качестве атрибута блоку нужно изображение/поверхность
        self.image.fill(color)
        self.rect = self.image.get_rect()  # и прямоугольник-область наслудемый от него.

    def get_x(self):  # Считывание X области
        return self.rect.x

    def set_x(self, x):  # Изменение X области
        self.rect.x = x

    def get_y(self):  # Считывание Y области
        return self.rect.y

    def set_y(self, y):  # Изменение Y области
        self.rect.y = y

    def set_color(self, color):  # Изменение цвета
        self.image.fill(color)


window = Window()
window.on_start()
