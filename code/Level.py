import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        # Pega a lista de backgrounds e adiciona na entity_list
        self.entity_list.extend(EntityFactory.get_entity('level_bg'))

    def run(self):
        # Adiciona som ao nivel 1
        pygame.mixer_music.load('./asset/menu_sound.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            # Desenha cada uma das imagens
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.flip()

        pass