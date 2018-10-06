DELIMITER = '\n\t'

def stop_words():
    with open('./../resources/stop_words.csv', 'r') as stop_words_file:
        stop_words = stop_words_file.readline().split(',')
        return stop_words

def is_stop_word(word):
    return word in stop_words()
