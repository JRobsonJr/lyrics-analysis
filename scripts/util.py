def get_stop_words():
    with open('./../resources/stop_words.csv', 'r') as file:
        stop_words = file.readline().split(',')
        return stop_words

def is_stop_word(word):
    stop_words = get_stop_words()
    return word in stop_words
