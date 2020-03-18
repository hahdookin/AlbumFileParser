"""
 - Go through each line of the file
 - Split the lines into ["artist", "album", "score"]
    - score in [5/5] or 5/5 form IDK yet
 - sort artists names and add to set, dictionary, or list
 - Add albums
"""
album_ascii = """
  ___   _     ______ _   ____  ___ _____ 
 / _ \ | |    | ___ \ | | |  \/  |/  ___|
/ /_\ \| |    | |_/ / | | | .  . |\ `--. 
|  _  || |    | ___ \ | | | |\/| | `--. \ 
| | | || |____| |_/ / |_| | |  | |/\__/ /
\_| |_/\_____/\____/ \___/\_|  |_/\____/ 
                                         
                                         """
def fractionToFloat(fracstr):
    x = fracstr.split('/')
    result = float(x[0]) / int(x[1])
    return result

def main():
    # Opens album text that I write to in 'r' mode
    albums = open("albums.txt", "r", encoding="utf8")

    # Opens the new file that will display data nicely in 'w' to overwrite existing data
    final_albums = open("Finished Sorted Albums.txt", "w", encoding="utf8")

    # Splits orginally file by "have listened:" section
    full_albums_lines = albums.readlines()
    albums_lines = full_albums_lines[full_albums_lines.index('have listened:\n') + 1:]

    # returns all the lines sorted alphabetically
    albums_lines.sort()

    # Stores artists added to final_albums
    written_artists = []

    final_albums.write(album_ascii)

    for line in albums_lines:
        # ex: ['the strokes', 'is this it', '[4/5]\n']
        split_line = line.split(' - ')

        artist = split_line[0]
        album_title = split_line[1]

        score = split_line[-1][:-1]

        # In case there is a space at the end of the line
        if " " in score:
            score = score[:-1]

        # String that we can do math with, ex: [4/5] => 4/5, then math is done
        score_workable = round(fractionToFloat(score[1:-1]) * 100, 2)

        if artist not in written_artists:
            written_artists.append(artist)
            final_albums.write(f"\n• {artist}:\n") # Gotta average artist score soon

        final_albums.write(f"  + {album_title} - {score_workable}%\n")

    albums.close()

if __name__ == "__main__":
    main()