from code.Entity import Entity
from code.Const import WIN_WIDTH


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= 3
