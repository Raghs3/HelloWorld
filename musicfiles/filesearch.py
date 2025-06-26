import os
import fnmatch


def find_albums(root, artist_name):
    caps_name = artist_name.upper()  # for case preserving like mac
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):  # generator expressions
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):  # works on linux
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:  # no need to walk as we know the dir, might not be efficient
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "black*")  # fnmatch filter can find files containing black by putting `*`
song_list = find_songs(album_list)  # filter sensitivity based on file system

for s in song_list:
    print(s)

# for a in album_list:
#     print(a)
