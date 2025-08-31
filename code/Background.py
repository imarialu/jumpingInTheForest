from code.Entity import Entity
from code.Const import WIN_WIDTH


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= 3
        # Se o canto direito chegar no esquerdo, a imagem é jogada para a direita novamente
        # criando o efeito de movimento
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
