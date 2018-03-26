from collections import Counter
from analysable import Analysable


class Album(Analysable):
    def __init__(self, title, artist, songs):
        self.title = title
        self.artist = artist
        self.songs = songs
        self.vocab = self.get_vocab()
        self.word_freq = Counter(self.vocab)

    def __str__(self):
        to_string = self.title + ', by ' + self.artist + '\n'

        for song in self.songs:
            to_string += '# ' + str(song) + '\n'

        return to_string

    def get_vocab(self):
        vocab = []
        for song in self.songs:
            for word in song.vocab:
                vocab.append(word)
        return vocab

    def get_word_freq_per_song(self, word):
        word_frequency = []

        for song in self.songs:
            word_frequency.append(song.get_word_frequency(word))

        return word_frequency

    def is_one_song_exclusive(self, word):
        word_frequency = self.get_word_freq_per_song(word)
        temp_counter = Counter(word_frequency)

        if temp_counter.get(0) == len(self.songs) - 1:
            return True
        else:
            return False
