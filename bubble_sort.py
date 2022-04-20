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

        self._height_for_find = 180  # Высота искомого блока
        self._next_block = 0  # Переменная счетчик
        self._go_to_find = True  # Переменная флаг продолжение "поиска"

        self._color_of_block_standard = (155, 155, 200)  # Стандартный цвет блока
        self._color_of_block_current = (200, 155, 155)  # Цвет текщего блока
        self._color_of_block_was_find = (155, 200, 155)  # Цвет найденного блока

        self._number_of_blocks = 20  # Количество элнментов в списке блоков
        self.blocks = []  # Пустой список
        self.xs_of_blocks = []  # Пустой список для перемешивания координат

        self._was_swapped = False  # Флаг "была перестановка"
        self._stop_sort = True  # Флаг "стоп сортировка"
        self._inner_counter = 0  # начало списка
        self._outer_counter = self._number_of_blocks - 1  # Конец списка

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

    def shuffle(self):  # Метод перемешивание
        random.shuffle(self.xs_of_blocks)  # Функция "перемешивание списка" из модуля import
        for i, x in enumerate(self.xs_of_blocks):  # Создаем кортежи из порядкового номера и координаты
            self.blocks[i].set_x(x)  # Подставляем в блоки по порядку "перемешанные" координаты

    def on_loop(self):  # В цикле
        if self._outer_counter > 0 and not self._stop_sort:  # Проверка необходимости продолжать сортировку
            self.blocks[self._inner_counter - 1].set_color(self._color_of_block_standard)  # Возвращаем стандатный цвет
            # Проверяем координаты соседних блоков
            if self.blocks[self._inner_counter].get_x() > self.blocks[self._inner_counter + 1].get_x():
                # Если первая больше второй - выделяем цветом  и меняем местами
                self.blocks[self._inner_counter].set_color(self._color_of_block_current)  # выделяем 1
                self.blocks[self._inner_counter + 1].set_color(self._color_of_block_was_find)  # выделяем 2
                min_of_x = self.blocks[self._inner_counter + 1].get_x()  # временная переменная для хранения
                self.blocks[self._inner_counter + 1].set_x(self.blocks[self._inner_counter].get_x())  # Заменяем 2
                self.blocks[self._inner_counter].set_x(min_of_x)  # Заменяем 1
                self._was_swapped = True  # Флаг "была перестановка"

            self._inner_counter += 1  # Переходим к следующему элементу

            if not (self._inner_counter < self._outer_counter):  # Если дошли до последнего элемента
                if not self._was_swapped:  # Проверяем была ли перестановка
                    self._stop_sort = True  # Если не было, то флаг "стоп сортировка" в значение True
                else:  # Иначе
                    self._was_swapped = False  # Сброс флага "была перестановка"
                    self._outer_counter -= 1  # Уменьшаем границу на 1
                    self.blocks[self._inner_counter - 1].set_color(self._color_of_block_standard)  # Возвращаем цвет
                    self.blocks[self._inner_counter].set_color(self._color_of_block_standard)  # Возвращаем цвет
                    self._inner_counter = 0  # Возвращаем нижнюю границу к первому элементу списка

    def on_event(self, event):  # Метод обработка событий
        if event.type == pygame.QUIT:  # Проверяем тип события
            self._running = False  # Выполняем действие
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:  # Проверяем событие и key
            self.shuffle()  # Перемешиваем
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            self.on_press_k_2()

    def on_press_k_2(self):
        self._was_swapped = False  # Флаг "была перестановка"
        self._stop_sort = False  # Флаг "стоп сортировка"
        self._inner_counter = 0  # начало списка
        self._outer_counter = self._number_of_blocks - 1  # Конец списка

    def on_render(self):  # Метод вывода на экран
        self._display_surf.fill(self._display_surf_color)  # Если требуется обновляем заливку
        for block in self.blocks:  # С помощью цикла
            self._display_surf.blit(block.image, block.rect)  # Выводим на экран блоки
        pygame.display.flip()  # Обновление

    def on_start(self):  # Метод запуск основного цикла
        self.on_init()  # Вызов изменения атрибутов
        while self._running:  # Проверяем атрибут "работа цикла"
            self._clock.tick(10)  # Вызываем метод tick()
            for event in pygame.event.get():  # Считываем действия с помощью метода get()
                self.on_event(event)  # Вызываем обработчик событий
            self.on_loop()
            self.on_render()  # Вызываем перерисовку
        Window.on_cleanup()  # Завершение программы происходит после выхода из основного цикла


window = Window()
window.on_start()
