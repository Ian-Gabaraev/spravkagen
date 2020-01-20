# Here the links are generated
from settings import cyrillic_to_unicode


class Translate:
    def __init__(self, cyrillic=None, numeric=None):
        self.cyrillic = cyrillic
        self.numeric = numeric

    # Replace each cyrillic character with its hexadecimal
    # value in the cyrillic_to_unicode dictionary.
    # Then convert the result into a string and return it.
    def translate_cyrillic_to_unicode(self):
        mapped = map(lambda character: cyrillic_to_unicode[character], tuple(self.cyrillic))
        return "".join(list(mapped))

    def translate_numeric(self):
        pass
