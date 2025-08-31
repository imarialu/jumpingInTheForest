import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import EVENT_OBSTACLE


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        # Pega a lista de backgrounds e adiciona na entity_list
        self.entity_list.extend(EntityFactory.get_entity('level_bg'))
        self.entity_list.append(EntityFactory.get_entity('player'))
        pygame.time.set_timer(EVENT_OBSTACLE, 1000)

    def run(self):
        # Adiciona som ao nivel 1
        pygame.mixer_music.load('./asset/menu_sound.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(100)
            # Desenha cada uma das imagens
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_OBSTACLE:
                    self.entity_list.append(EntityFactory.get_entity('obstacle_1'))
            pygame.display.flip()

        pass