text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

# use map
map_capitals = list(map(str.upper, text))
print(map_capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

# use map
map_words = list(map(str.upper, text.split(' ')))
print(map_words)

for x in map(str.upper, text.split(' ')):  # directly iterate over map iterable object instead of converting iterable to list
    print(x)
