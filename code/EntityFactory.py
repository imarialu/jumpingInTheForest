from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level_bg':
                list_bg = [] # Lista vazia
                # Pega cada background e adiciona na lista
                for i in range(7):
                    # Adiciona os objetos da classe Background
                    list_bg.append(Background(f'level_bg{i}', (0, 0)))
                    list_bg.append(Background(f'level_bg{i}', (WIN_WIDTH, 0)))
                return list_bg
