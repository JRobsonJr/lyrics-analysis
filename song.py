from collections import Counter

class Song:
    def calculate_frequency(self):
        for k, v in dict(Counter(self.vocab)).iteritems():
            self.inv_freq[v] = self.inv_freq.get(v, [])
            self.inv_freq[v].append(k)
    
    def get_most_common(self):
        keys = self.inv_freq.keys()
        keys = sorted(keys, reverse=True)
        return (self.inv_freq.get(keys[0]), keys[0]), (self.inv_freq.get(keys[1]), keys[1]), (self.inv_freq.get(keys[2]), keys[2])
    
    def get_unique(self):
        keys = self.inv_freq.keys()
        keys = sorted(keys)
        if keys[0] == 1:
            return self.inv_freq.get(keys[0])
        else:
            return "no unique words"

    def contains_word(self, query):
        for word in self.vocab:
            if word == query:
                return True
        return False

    def __init__(self, title, vocab):
        self.title = title
        self.vocab = vocab
        self.inv_freq = {}

        self.calculate_frequency()