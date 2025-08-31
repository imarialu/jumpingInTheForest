import pygame.key

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.jump = False
        self.speed = 12
        self.gravity = 1

    def move(self, enemy):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.rect.y == 190 and self.jump == False:
                self.jump = True

        if keys[pygame.K_LEFT]:
            if not self.rect.x <= 0:
                self.rect.x -= 3

        if keys[pygame.K_RIGHT]:
            if not self.rect.x >= 560:
                self.rect.x += 3

        if self.jump:
            self.rect.y -= self.speed
            self.speed -= self.gravity

        if self.rect.y == 190 and self.jump:
            self.jump = False
            self.speed = 12

        for ent in enemy:
            if ent.name == 'obstacle_1':
                if self.rect.colliderect(ent):
                    return False

        pass
