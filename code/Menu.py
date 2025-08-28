import pygame.image
from code.Const import WIN_WIDTH, COLOR_MENU_TITLE, MENU_OPTION, COLOR_MENU_OPTION, COLOR_SELECTED_OPTION
from pygame.font import Font
from pygame import Surface, Rect

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu_bg.png')
        self.rect = self.surf.get_rect()

    def run(self):
        menu_option = 0
        # Adiciona som ao menu
        pygame.mixer_music.load('./asset/menu_sound.wav')
        pygame.mixer_music.play(-1)

        while True:
            # Desenha a imagem
            self.window.blit(source=self.surf, dest=self.rect)  # "Desenha" a imagem no retângulo

            # Adicionando e estlizando o texto do menu
            self.menu_text(50, "jumping", COLOR_MENU_TITLE, ((WIN_WIDTH / 2), 70))
            self.menu_text(30, "in the", COLOR_MENU_TITLE, ((WIN_WIDTH / 2), 110))
            self.menu_text(50, "Forest", COLOR_MENU_TITLE, ((WIN_WIDTH / 2), 140))

            # Adicionando e estlizando as opções do menu
            for i in range(len(MENU_OPTION)):
                # Adiciona outra cor a opção selecionada
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_SELECTED_OPTION, ((WIN_WIDTH / 2), 220 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_MENU_OPTION, ((WIN_WIDTH / 2), 220 + 30 * i))
            # Atualiza a tela
            pygame.display.flip()

            # Checa os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Finaliza o pygame
                # Adiciona o evento de seleção
                if event.type == pygame.KEYDOWN:
                    # Seleção com a rolagem para baixo
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    # Seleção com a rolagem para cima
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    # Retorna ao inicio do menu
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)