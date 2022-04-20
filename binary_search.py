import pygame
from tools import Block  # Импорт класса Block из модуля tools


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
        self.block = Block(size=self._size_of_block, color=(155, 155, 200))  # Создаем объект класса Block

        self._height_for_find = 180  # Высота искомого блока
        self._next_block = 0  # Переменная счетчик
        self._go_to_find = True  # Переменная флаг продолжение "поиска"

        self._color_of_block_standard = (155, 155, 200)  # Стандартный цвет блока
        self._color_of_block_current = (200, 155, 155)  # Цвет текщего блока
        self._color_of_block_was_find = (155, 200, 155)   # Цвет найденного блока

        self._number_of_blocks = 20  # Количество элнментов в списке блоков
        self.blocks = []  # Пустой список

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
                               color=self._color_of_block_standard)   # Высота растет на 10 с каждой итерацией
            temp_block.set_x(200 + i * 11)  # По X сдвигаем вправо каждый шаг
            temp_block.set_y(300 - i * 10)  # По Y сдвигаем вверх на 10 еаждый шаг
            self.blocks.append(temp_block)  # Добавляем блок к списку

    def on_loop(self):  # В цикле
        if self._go_to_find:
            # Возвращаем стандартный цвет блоку из предыдущей итерации
            self.blocks[self._middle_of_list].set_color(self._color_of_block_standard)
            self._middle_of_list = int((self._high_of_list + self._low_of_list) / 2) # Находим середину списка
            self.blocks[self._middle_of_list].set_color(self._color_of_block_current)  # Отмечаем проверяемый блок

        if self.blocks[self._middle_of_list].rect.height == self._height_for_find:  # Проверка высоты
            self._go_to_find = False  # Если искомая, то заканчиваем поиск
            self.blocks[self._middle_of_list].set_color(self._color_of_block_was_find)  # Отмечаем найденый блок

        # При переходе к новой итерации сдвигаем границу поиска
        if self.blocks[self._middle_of_list].rect.height > self._height_for_find:
            self._high_of_list = self._middle_of_list - 1  # Влево если искомое значение меньше текущего
        else:
            self._low_of_list = self._middle_of_list + 1  # Вправо если искомое значение больше текущего

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


window = Window()
window.on_start()