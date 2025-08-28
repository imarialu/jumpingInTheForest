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
        while True:
            # Desenha cada uma das imagens
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()

        pass