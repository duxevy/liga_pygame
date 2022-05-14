import pygame
import config
import utils
from tools import Block


class Window:  # Создаем класс для поверхности рисования

    def __init__(self):
        pygame.init()  # Инициализируем Pygame
        self._running = True  # атрибут работа цикла - True
        self._size = self.width, self.height = 640, 480  # Задаем длину и ширину окна
        self._display_surf_color = (0, 0, 0)  # Цвет заливки
        self._display_surf = pygame.display.set_mode(self._size)  # Создаем окно
        self._clock = pygame.time.Clock()  # Добавляем в инициализацию окна атрибут "таймер"
        # self.main_menu_buttons = utils.create_menu(config.button)

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_init(self):
        self._display_surf.fill(self._display_surf_color)  # Заполняем окно цветом

     # def on_loop(self):

    def on_event(self, event):  # Метод обработка событий
        if event.type == pygame.QUIT:  # Проверяем тип события
            self._running = False  # Выполняем действие

    def on_render(self):  # Метод вывода на экран
        self._display_surf.fill(self._display_surf_color)  # Если требуется обновляем заливку
        for btn in self.main_menu_buttons:  # С помощью цикла
            btn.is_touched()  # перерисовка, если навели мышку
            self._display_surf.blit(btn.image, btn.rect)  # Рисуем кнопки
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
