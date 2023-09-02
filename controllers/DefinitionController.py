from models.definition_model import DefinitionModel

class DefinitionController:
    def __init__(self):
        self.model = DefinitionModel()

    def insert_definition(self, word, definition):
        self.model.insert_definition(word, definition)
