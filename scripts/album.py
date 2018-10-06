from collections import Counter
from analysable import Analysable


class Album(Analysable):
    def __init__(self, title, artist, songs):
        super(Album, self).__init__(title, [])
        self.artist = artist
        self.songs = songs
        self.vocab = self.retrieve_vocab()
        self.word_freq = Counter(self.vocab)

    def __str__(self):
        to_string = self.title + ', by ' + self.artist + '\n'

        for song in self.songs:
            to_string += '# ' + str(song) + '\n'

        return to_string

    def retrieve_vocab(self):
        vocab = []
        for song in self.songs:
            for word in song.vocab:
                vocab.append(word)
        return vocab

    def word_freq_per_song(self, word):
        word_frequency = []

        for song in self.songs:
            word_frequency.append(song.count(word))

        return word_frequency

    def bigram_freq_per_song(self, bigram):
        bigram_freq = []

        for song in self.songs:
            bigram_freq.append(song.count_bigram(bigram))

        return bigram_freq

    def is_one_song_exclusive(self, word):
        word_frequency = self.word_freq_per_song(word)
        temp_counter = Counter(word_frequency)

        return temp_counter.get(0) == len(self.songs) - 1

    def is_one_song_exclusive_bigram(self, bigram):
        bigram_frequency = self.bigram_freq_per_song(bigram)
        temp_counter = Counter(bigram_frequency)

        return temp_counter.get(0) == len(self.songs) - 1
