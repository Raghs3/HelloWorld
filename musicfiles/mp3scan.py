import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f'*.{extension}'):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)         # use it in yielded values


# for f in find_music('music', 'emp3'):
#     print(f)
# can use generators in for loop and take care of creating the generator, for loop creates generator and calling next

# could have done this too
#
my_music_files = find_music('music', 'emp3')

for f in my_music_files:
    id3r = id3reader.Reader(f)
    print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
        id3r.get_value('performer'),
        id3r.get_value('album'),
        id3r.get_value('track'),
        id3r.get_value('title')
    ))
