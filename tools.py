from pygame import Surface


# Класс блока, который будет элементом в визуализациях будущих алгоритмах поиска и сортировки
class Block():

    def __init__(self, size=(0, 0), color=(0, 0, 0)):
        self.image = Surface(size)  # В качестве атрибута блоку нужно изображение/поверхность
        self.image.fill(color)
        self.rect = self.image.get_rect()  # и прямоугольник наслудемый от него.

    def get_x(self):
        return self.rect.x

    def set_x(self, x):
        self.rect.x = x

    def get_y(self):
        return self.rect.y

    def set_y(self, y):
        self.rect.y = y

    def set_color(self, color):
        self.image.fill(color)
