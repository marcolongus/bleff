from models.definition_model import DefinitionModel

class DefinitionController:
    def __init__(self):        
        self.model = DefinitionModel()

    def save_definition(self, word, definition):
        self.model.add_definition(word, definition)
