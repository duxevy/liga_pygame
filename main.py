import pygame

pygame.init()

screen_size = width, height = 800,600
screen = pygame.display.set_mode(screen_size)

BLACK = (0, 0, 0)
screen.fill(BLACK)

size_of_block = height_block, width_block = 100, 100
color = (152, 255, 152)
body_block = pygame.Surface(size_of_block)
body_block.fill(color)

rect_of_block = body_block.get_rect()

rect_of_block.x = 350
rect_of_block.y = 250

screen.blit(body_block, rect_of_block)

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()