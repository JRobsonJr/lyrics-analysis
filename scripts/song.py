from collections import Counter
from analysable import Analysable


class Song(Analysable):
    def __init__(self, title, vocab):
        super(Song, self).__init__(title, vocab)
