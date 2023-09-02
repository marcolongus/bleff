from models.definition_model import DefinitionModel
from models.dictionary_model import DictionaryModel

class DefinitionController:
    """ Handle definitions written by user and dict and R/W them into database """

    def __init__(self):        
        self.definition = DefinitionModel()
        self.dictionary = DictionaryModel()

    def save_definition(self, word, definition):
        self.definition.add_definition(word, definition)

    def provide_word_to_define(self):
        return self.dictionary.get_random_word()
