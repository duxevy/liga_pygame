import pygame


class Window:  # Создаем класс для поверхности рисования

    def __init__(self):  # Инициализация ообъекта: задаем атрибуты
        pygame.init()  # Инициализируем Pygame
        self._running = True  # атрибут работа цикла - True
        self._size = self.width, self.height = 640, 480  # Задаем длину и ширину окна
        self._display_surf_color = (0, 0, 0)  # Цвет заливки
        self._size_of_block = self.height_of_block, self.width_of_block = 100, 100  # Размеры блока
        self._direction_of_movement_x = 1  # Направление движения по X
        self._direction_of_movement_y = 1  # Направление движения по Y
        self._display_surf = pygame.display.set_mode(self._size)  # Создаем окно
        self._clock = pygame.time.Clock()  # Добавляем в инициализацию окна атрибут "таймер"
        self.block_1 = Block(size=self._size_of_block, color=(155, 155, 200))  # Создаем объект класса Block
        self.block_2 = Block(size=self._size_of_block, color=(200, 155, 155))

    @staticmethod  # Эта метка говорит о том, что метод статический. Он не изменяет никакие объекты,
    # а работает только с параметрами, которые в него передали.
    def on_cleanup():  # Метод завершения программы
        pygame.quit()

    # Создаем метод для изменения атрибутов у объектов-атрибутов, которые были созданы при инициализации
    def on_init(self):
        self._display_surf.fill(self._display_surf_color)  # Заполняем окно цветом
        self.block_1.set_x(230)  # Установим координату X для блока1
        self.block_1.set_y(190)  # Установим координату Y для блока1
        self.block_2.set_x(280)  # Установим координату X для блока2
        self.block_2.set_y(190)  # Установим координату Y для блока2

    def on_loop(self):  # Метод движение
        if self.block_1.get_x() == 340:  # Если позиция левого верхнего угла равна 340
            self._direction_of_movement_x = -1  # То, будем двигать влево - умееньшать значение позиции X
        elif self.block_1.get_x() == 230:  # Если позиция левого угла по X = 230
            self._direction_of_movement_x = 1  # То, будем двигать вправо - увеличивать значение позиции X
        self.block_1.set_x(self.block_1.get_x() + 1 * self._direction_of_movement_x)  # Изменяем позицию по X

        if self.block_2.get_y() == 240:  # Если позиция левого верхнего угла равна 340
            self._direction_of_movement_y = -1  # То, будем двигать вверх - умееньшать значение позиции Y
        elif self.block_2.get_y() == 140:  # Если позиция левого угла по y = 240
            self._direction_of_movement_y = 1  # То, будем двигать вниз - увеличивать значение позиции Y
        self.block_2.set_y(self.block_2.get_y() + 1 * self._direction_of_movement_y)  # Изменяем позицию по Y

    def on_event(self, event):  # Метод обработка событий
        if event.type == pygame.QUIT:
            self._running = False

    def on_render(self):  # Метод вывода на экран
        self._display_surf.fill(self._display_surf_color)  # Если требуется обновляем заливку
        self._display_surf.blit(self.block_1.image, self.block_1.rect)  # Перерисовка фигуры
        self._display_surf.blit(self.block_2.image, self.block_2.rect)
        pygame.display.flip()  # Обновление

    def on_start(self):  # Метод запуск основного цикла
        self.on_init()  # Вызов изменения атрибутов
        while self._running:  # Проверяем атрибут "работа цикла"
            self._clock.tick(60)  # Вызываем метод tick()
            for event in pygame.event.get():
                self.on_event(event)  # Вызываем обработчик событий
            self.on_loop()  # Движение блока
            self.on_render()  # Вызываем перерисовку
        Window.on_cleanup()  # Завершение программы происходит после выхода из основного цикла


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
