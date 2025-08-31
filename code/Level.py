import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import EVENT_OBSTACLE, COLOR_MENU_TITLE
from pygame.font import Font
from pygame import Surface, Rect


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        # Pega a lista de backgrounds e adiciona na entity_list
        self.entity_list.extend(EntityFactory.get_entity('level_bg'))
        self.player = self.entity_list.append(EntityFactory.get_entity('player'))
        pygame.time.set_timer(EVENT_OBSTACLE, 1500)

    def run(self):
        # Adiciona som ao nivel 1
        pygame.mixer_music.load('./asset/menu_sound.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        pontos = 0
        while True:
            clock.tick(100)
            # Desenha cada uma das imagens
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if ent.name == 'player':
                    player_return = ent.move(self.entity_list)
                    if player_return == False:
                        from code.Game import Game
                        game = Game()
                        game.run()
                else:
                    ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_OBSTACLE:
                    pontos += 1
                    self.entity_list.append(EntityFactory.get_entity('obstacle_1'))

            self.menu_text(16, "PONTOS: ", COLOR_MENU_TITLE, (50, 300))
            self.menu_text(16, f"{pontos}", COLOR_MENU_TITLE, (90, 300))

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)