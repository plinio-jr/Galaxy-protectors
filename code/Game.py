import pygame

from code.Menu import Menu
from code.Const import MIN_WIDTH, MIN_HEIGHT


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(MIN_WIDTH, MIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()