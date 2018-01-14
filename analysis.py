from song import Song

title = ""
vocab = []
songs = []

def clean_string(incomingString):
    unwanted_chars = [",", '\"', "(", ")", "?", "!", "...", ".", ":", "-"]
    clean_string = incomingString.lower()
    
    for i in xrange(len(unwanted_chars)):
        clean_string = clean_string.strip(unwanted_chars[i])
    
    return clean_string

def get_lyrics():
    file = open("resources/reputation_lyrics.txt","r") 
    file_lines = file.readlines()
    file.close()
    return file_lines

def add_song(title, vocab):
    new_song = Song(title.strip(), vocab)
    songs.append(new_song)

file_lines = get_lyrics()

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

file = open("output/analysis_result.txt","w") 

vocab = []

for i in xrange(len(songs)):
    for j in xrange(len(songs[i].vocab)):
        vocab.append(songs[i].vocab[j])

    file.write("#" + str(i + 1) + " " + songs[i].title + ":\n")
    file.write("MOST COMMON WORD(S): " + str(songs[i].get_most_common()) + '\n')
    file.write(str(songs[i].inv_freq) + '\n\n\n')

album = Song(1, vocab)
file.write("OVERALL:\n")
file.write("MOST COMMON WORD: " + str(album.get_most_common()) + '\n')
file.write(str(album.inv_freq) + '\n\n\n')

unique_words = album.get_unique()

file.write("UNIQUE SONGS ANALYSIS:\n")
for i in xrange(len(songs)):
    file.write("#" + str(i + 1) + " " + songs[i].title + ":\n")
    album_uniques = []
    for j in xrange(len(unique_words)):
        if (songs[i].contains_word(unique_words[j])):
            album_uniques.append(unique_words[j])
    file.write(str(album_uniques) + '\n' + str((100.0 * len(album_uniques))/len(songs[i].vocab)) + " percent (" + str(len(album_uniques)) + ") unique words. \n")

file.close()