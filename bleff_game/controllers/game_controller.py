from bleff_game.models.game_model import GameModel


class GameController:
    def __init__(self, name):
        self.name = name

    def create_game(self):
        GameModel.create_game(self.name)
