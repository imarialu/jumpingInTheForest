from code.Entity import Entity

class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

    def run(self):
        pass