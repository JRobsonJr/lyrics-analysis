from collections import Counter
from abc import ABC

from util import is_stop_word


class Analysable(ABC):
    def __init__(self, title, vocab):        
        self.title = title
        self.vocab = vocab
        self.word_freq = Counter(self.vocab)
        super(Analysable, self).__init__()

    def __str__(self):
        total_words = len(self.vocab)
        unique_words = len(self.get_unique_words())
        non_stop_words = len(self.get_non_stop_words())
        perc_unique = str(int(100.0 * unique_words / total_words)) + '%'
        perc_non_stop = str(int(100.0 * non_stop_words / total_words)) + '%'
        return self.title + '\n\tTotal words: ' + str(total_words) + \
            '\n\tUnique words: ' + str(unique_words) + ' (' + perc_unique + ')' + \
            '\n\tNot stop words: ' + str(non_stop_words) + ' (' + perc_non_stop + ')' + \
            '\n\tTop 5 words: ' + str(self.get_top_words(5))

    def get_most_common_words(self):
        return self.word_freq.most_common()

    def get_top_words(self, number):
        most_common_words = self.get_most_common_words()
        top_words = []
        index = 0

        while(len(top_words) != number):
            if (not is_stop_word(most_common_words[index][0])):
                top_words.append(most_common_words[index])
            index += 1

        return top_words

    def get_unique_words(self):
        return set(self.vocab)

    def get_unique_words_in_order(self):
        unique_words = []

        for word in self.vocab:
            if word not in unique_words:
                unique_words.append(word)
        
        return unique_words

    def contains_word(self, word):
        return word in self.vocab

    def get_word_frequency(self, word):
        if self.word_freq.get(word):
            return self.word_freq.get(word)
        else:
            return 0

    def get_non_stop_words(self):
        non_stop_words = []
        for word in self.vocab:
            if (not is_stop_word(word)):
                non_stop_words.append(word)
        return non_stop_words
