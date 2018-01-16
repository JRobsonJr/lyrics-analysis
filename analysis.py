from song import Song

title = ""
vocab = []
songs = []
resource = "taylor_swift_red"

def clean_string(string):
    unwanted_chars = [",", '\"', "(", ")", "?", "!", "...", ".", ":", "-"]
    clean_string = string.lower()
    
    for i in xrange(len(unwanted_chars)):
        clean_string = clean_string.strip(unwanted_chars[i])
    
    return clean_string

def get_lyrics():
    file = open("resources/lyrics/" + resource + ".txt", "r") 
    file_lines = file.readlines()
    file.close()

    return file_lines

def add_song(title, vocab):
    new_song = Song(title.strip(), vocab)
    songs.append(new_song)

def instantiate_songs(file_lines):
    for i in xrange(1, len(file_lines)):
        current_line = file_lines[i].split()

        if (len(current_line) == 0 or current_line[0][0] == "["):
            continue
        elif (current_line[0][0] == "#"):
            if (title != ""):
                add_song(title, vocab)
                title = ""
                vocab = []
            for i in xrange(1, len(current_line)):
                title += current_line[i] + " "
        else:
            for i in xrange(len(current_line)):
                vocab.append(clean_string(current_line[i]))

    add_song(title, vocab)

def main():
    file_lines = get_lyrics()
    instantiate_songs(file_lines)

    file = open("output/result_" + resource + ".txt", "w") 

    vocab = []
    
    for i in xrange(len(songs)):
        current_song = songs[i]
        file.write("#" + str(i + 1) + " " + current_song.title + ":\n")
        file.write("MOST COMMON WORD(S): " + str(current_song.get_most_common()) + '\n')
        file.write(str(current_song.inv_freq) + '\n\n\n')

    for i in xrange(len(songs)):
        current_song = songs[i]
        
        for j in xrange(len(current_song.vocab)):
            vocab.append(current_song.vocab[j])
    album = Song(1, vocab)
    file.write("OVERALL:\n")
    file.write("MOST COMMON WORDS: " + str(album.get_most_common()) + '\n')
    file.write(str(album.inv_freq) + '\n\n\n')

    unique_words = album.get_unique()

    file.write("UNIQUE SONGS ANALYSIS:\n")
    file.write("OVERALL UNIQUE SONGS: " + str(unique_words) + "\n" + str(len(unique_words)) + " unique words out of " + str(len(vocab)) + "\n")
    
    for i in xrange(len(songs)):
        current_song = songs[i]
        file.write("#" + str(i + 1) + " " + current_song.title + ":\n")
        album_uniques = []
        for j in xrange(len(unique_words)):
            if (current_song.contains_word(unique_words[j])):
                album_uniques.append(unique_words[j])
        file.write(str(album_uniques) + '\n' + str((100.0 * len(album_uniques))/len(unique_words)) + " percent (" + str(len(album_uniques)) + ") unique words. \n")

    file.close()

if __name__ == "__main__":
    main()