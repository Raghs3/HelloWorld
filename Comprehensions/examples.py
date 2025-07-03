text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]

print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')  # if you don't need to process no need for comprehension
print(lc_words)

lc_words = [word for word in text.split(' ')]
print(lc_words)  # don't do this, unnecessary and inefficient
