import pygame

def initialize_display(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Symbol Translator")
    return screen

def update_display(screen, frame):
    screen.blit(pygame.surfarray.make_surface(frame.swapaxes(0, 1)), (0, 0))
    pygame.display.update()
