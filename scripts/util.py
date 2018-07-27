DELIMITER = '\n\t'

def get_stop_words():
    with open('./../resources/stop_words.csv', 'r') as stop_words_file:
        stop_words = stop_words_file.readline().split(',')
        return stop_words

def is_stop_word(word):
    stop_words = get_stop_words()
    return word in stop_words
