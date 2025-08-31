from code.Background import Background
from code.Player import Player
from code.Obstacle import Obstacle
from code.Const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level_bg':
                list_bg = [] # Lista vazia
                # Pega cada background e adiciona na lista
                for i in range(5):
                    # Adiciona os objetos da classe Background
                    list_bg.append(Background(f'level_bg', (0, 0)))
                    list_bg.append(Background(f'level_bg', (WIN_WIDTH, 0)))
                return list_bg
            case 'player':
                return Player('player', (10, 190))
            case 'obstacle_1':
                return Obstacle('obstacle_1', (WIN_WIDTH + 4, 190))
