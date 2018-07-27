# coding:utf-8

import sys

from song import Song
from album import Album
from util import is_stop_word


def clean_string(string):
    unwanted_chars = [',', '\"', '(', ')', '?', '!', '...', '.', ':', '-', '—']
    string = string.lower()
    for unwanted_char in unwanted_chars:
        string = string.strip(unwanted_char)
    return string


def get_lyrics(resource):
    with open('../resources/lyrics/' + str(resource), 'r', encoding='utf-8') as lyrics_file:
        file_lines = lyrics_file.readlines()
    return file_lines


def instantiate_songs(file_lines):
    title = ''
    vocab = []
    songs = []

    for line_index in range(1, len(file_lines)):
        line = file_lines[line_index]
        line_words = line.split()

        if not (line_words or line_words[0][0] == '['):
            if line_words[0][0] == '#':
                if title != '':
                    new_song = Song(title.strip(), vocab)
                    title = ''
                    vocab = []
                    songs.append(new_song)
                for i in range(1, len(line_words)):
                    title += line_words[i] + ' '
            else:
                for word in line_words:
                    vocab.append(clean_string(word))

    new_song = Song(title.strip(), vocab)
    songs.append(new_song)

    return songs


def write_word_frequency(lyrics_file, album):
    lyrics_file.write('OVERALL:\n')

    for (word, value) in album.get_most_common_words():
        if (not is_stop_word(word) and not album.is_one_song_exclusive(word)):
            lyrics_file.write(
                word + ' ' + str(album.get_word_freq_per_song(word)) + ' Ov: ' + str(value) + '\n')

    lyrics_file.write('\n')

def write_bigram_frequency(lyrics_file, album):
    lyrics_file.write('OVERALL:\n')

    for (bigram, value) in album.get_most_common_bigrams():
        if not album.is_one_song_exclusive_bigram(bigram):
            lyrics_file.write(
                str(bigram) + ' ' + str(album.get_bigram_freq_per_song(bigram)) +
                ' Ov: ' + str(value) + '\n')

    lyrics_file.write('\n')


def write_txt(path, album):
    with open(path, 'w', encoding='utf-8') as lyrics_file:
        songs = album.songs

        for song in songs:
            lyrics_file.write('# ' + song.title + '\n')
            lyrics_file.write(str(song.get_top_bigrams(10)) + '\n\n')
            ''' count = 0
            for word in song.get_unique_words_in_order():
                lyrics_file.write(word + ' ')
                count += 1
                if count % 10 == 0:
                    lyrics_file.write('\n')
            lyrics_file.write('\n\n') '''
        write_bigram_frequency(lyrics_file, album)
        perc = 100.0 * len(set(album.vocab)) / len(album.vocab)
        lyrics_file.write(str(len(album.get_unique_words())) + ' different words out of ' +
                          str(len(album.vocab)) + ' (' + str(int(perc)) + '%)\n')

        lyrics_file.write(str(album))


def main():
    resource = sys.argv[1]

    file_lines = get_lyrics(resource)
    songs = instantiate_songs(file_lines)
    album = Album('title', 'artist', songs)

    path = '../output/result_' + resource
    write_txt(path, album)


if __name__ == '__main__':
    main()
