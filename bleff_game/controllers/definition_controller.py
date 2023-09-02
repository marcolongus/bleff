from bleff_game.models.definition_model import DefinitionModel


class DefinitionController:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

    def save_definition(self):
        return DefinitionModel.add_definition(self.word, self.definition)
