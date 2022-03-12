import pygame


class Window:
    def __init__(self):
        pygame.init()
        self._running = True
        self._size = self.width, self.height = 640, 480
        self._display_surf_color = (0, 0, 0)
        self._display_surf = pygame.display.set_mode(self._size)
        self._display_surf.fill(self._display_surf_color)
        self._clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_render(self):
        self._display_surf.fill(self._display_surf_color)
        pygame.display.flip()

    def on_start(self):
        while self._running:
            self._clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        Window.on_cleanup()

    @staticmethod
    def on_cleanup():
        pygame.quit()


class Block:
    def __init__(self, size=(100, 100), color=(152, 255, 152)):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()


rect_of_block.x = 350
rect_of_block.y = 250

screen.blit(body_block, rect_of_block)
