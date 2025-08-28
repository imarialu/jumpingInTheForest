from code.Menu import Menu, MENU_OPTION
from code.Const import WIN_WIDTH, WIN_HEIGHT
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            # Caso a opção "EXIT" for escolhida, a janela é fechada
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass


