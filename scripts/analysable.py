from collections import Counter
from abc import ABC

from util import is_stop_word, DELIMITER


class Analysable(ABC):
    def __init__(self, title, vocab):
        self.title = title
        self.vocab = vocab
        self.word_freq = Counter(self.vocab)
        super(Analysable, self).__init__()

    def __str__(self):
        word_count = self.word_count()
        unique_words_count = self.unique_words_count()
        lexical_diversity = round(self.lexical_diversity(), 3)

        return self.title + \
            DELIMITER + 'Total words: ' + str(word_count) + \
            DELIMITER + 'Unique words: ' + str(unique_words_count) + \
            DELIMITER + 'Lexical diversity: ' + str(lexical_diversity) + \
            DELIMITER + 'Top 5 words: ' + str(self.top_n_words(5))

    def word_count(self):
        return len(self.vocab)

    def unique_words(self):
        return set(self.vocab)

    def sorted_unique_words(self):
        return sorted(self.unique_words)

    def unique_words_count(self):
        return len(self.unique_words())

    def lexical_diversity(self):
        word_count = self.word_count()
        unique_words_count = self.unique_words_count()
        return unique_words_count / word_count

    def most_common_words(self):
        return self.word_freq.most_common()

    def top_n_words(self, number):
        most_common_words = self.most_common_words()
        top_words = []
        index = 0

        while len(top_words) != number:
            if not is_stop_word(most_common_words[index][0]):
                top_words.append(most_common_words[index])
            index += 1

        return top_words

    def search(self, word):
        return word in self.vocab

    def count(self, word):
        return self.word_freq.get(word) if self.word_freq.get(word) else 0

    def ngrams(self, n):
        ngrams = []
        
        for i in range(len(self.vocab) - n + 1):
            ngram = []

            for j in range(n):
                ngram.append(self.vocab[i + j])

            ngrams.append(ngram)

        return ngrams

    def bigrams(self):
        bigrams = []

        for i in range(len(self.vocab) - 1):
            bigrams.append((self.vocab[i], self.vocab[i + 1]))

        return bigrams

    def most_common_bigrams(self):
        bigram_freq = Counter(self.bigrams())
        most_common_bigrams = bigram_freq.most_common()

        return most_common_bigrams

    def top_bigrams(self, number):
        most_common_bigrams = self.most_common_bigrams()
        top_bigrams = []
        index = 0

        while len(top_bigrams) != number:
            if (not is_stop_word(most_common_bigrams[index][0][0])
                    or not is_stop_word(most_common_bigrams[index][0][1])):
                top_bigrams.append(most_common_bigrams[index])
            index += 1

        return top_bigrams

    def count_bigram(self, bigram):
        bigram_freq = Counter(self.bigrams())
        return bigram_freq.get(bigram) if bigram_freq.get(bigram) else 0
