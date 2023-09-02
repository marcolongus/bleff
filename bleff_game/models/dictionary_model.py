import json
import random

class DictionaryModel():
    def __init__(self, path='dictionary.json'):
        self.path = path
        with open(self.path, 'r', encoding='utf-8') as file:
            self.dictionary = json.load(file)

    def get_random_word(self):
        return random.choice(list(self.dictionary.keys()))

    def get_definition(self, word):
        return self.dictionary.get(word, "Word not found")