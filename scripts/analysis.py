import sys

from song import Song
from album import Album
from util import is_stop_word


def clean_string(string):
    unwanted_chars = [',', '\"', '(', ')', '?', '!', '...', '.', ':', '-', '—']
    clean_string = string.lower()
    for i in range(len(unwanted_chars)):
        clean_string = clean_string.strip(unwanted_chars[i])
    return clean_string


def get_lyrics(resource):
    with open('../resources/lyrics/' + str(resource), 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
    return file_lines


def instantiate_songs(file_lines):
    title = ''
    vocab = []
    songs = []

    for i in range(1, len(file_lines)):
        current_line = file_lines[i].split()

        if not (len(current_line) == 0 or current_line[0][0] == '['):
            if (current_line[0][0] == '#'):
                if (title != ''):
                    new_song = Song(title.strip(), vocab)
                    title = ''
                    vocab = []
                    songs.append(new_song)
                for i in range(1, len(current_line)):
                    title += current_line[i] + ' '
            else:
                for i in range(len(current_line)):
                    vocab.append(clean_string(current_line[i]))

    new_song = Song(title.strip(), vocab)
    songs.append(new_song)

    return songs


def write_txt(path, album):
    with open(path, 'w', encoding='utf-8') as file:
        file.write('OVERALL:\n')
        for (word, value) in album.get_most_common_words():
            if (not is_stop_word(word) and not album.is_one_song_exclusive(word)):
                file.write(
                    word + ' ' + str(album.get_word_freq_per_song(word)) + ' Ov: ' + str(value) + '\n')

        file.write('\n')

        perc = 100.0 * len(set(album.vocab)) / len(album.vocab)
        file.write(str(len(album.get_unique_words())) + ' different words out of ' +
                   str(len(album.vocab)) + ' (' + str(int(perc)) + '%)\n')

        file.write(str(album))


def main():
    resource = sys.argv[1]

    file_lines = get_lyrics(resource)
    songs = instantiate_songs(file_lines)
    album = Album('title', 'artist', songs)

    path = '../output/result_' + resource
    write_txt(path, album)


if __name__ == '__main__':
    main()
