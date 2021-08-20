import re
import string
from utils import util_constants as util_const


class Fumes:
    """
    Instantiate a Fumes object.
    Text will be fumigated according to mention methods.

    :param methods: List of methods to include (default=None).
    :type methods: list
    """

    def __init__(self, methods: list = None):
        self.methods = methods

    def purge(self, text: string) -> string:
        """
        Fumigate the text

        :param text: The text to fumigate.
        :type text: string

        :return: The result after fumigation.
        :rtype: string
        """
        if self.methods is None:
            # for text in texts:
            text = text.lower()
            # Remove Symbols, Links, Numbers, Emojis
            text = re.sub(r"(@[A-Za-z0-9]+)|(\d+)|([^0-9A-Za-z ])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
            text = re.sub(r"\s+", " ", text)
            # remove StopWords
            text = " ".join([word for word in text.split() if word not in util_const.stopwords])
            return text
