import json
import random


with open("dictionary.json", 'r', encoding='utf-8') as file:
    dictionary = json.load(file)
    print(type(dictionary))
    print(dictionary['palabras'])
    print(dictionary.values())


class DictionaryModel():
    def __init__(self, path):
        self.path = path
        self.dictionary = None

    def load_dictionary(self):    
        with open(self.path, 'r', encoding='utf-8') as file:
            self.dictionary = json.load(file)

    def get_random_word(self):
        return random.choice(list(self.dictionary.values()))

    def get_definition(self, word):
        return self.dictionary.get(word, "Word not found")



# dictionary = DictionaryModel("dictionary.json")

# dictionary.load_dictionary()
# print(dictionary.get_random_word())
