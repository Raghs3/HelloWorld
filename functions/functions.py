def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)
    # print("spam and eggs")


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    # text = str(text)
    text = ""
    for arg in args:
        text += str(arg) + sep
    # text = text.rstrip(sep)  # if we want to remove the trailing colon, but will be solved using comprehensions so no need to do right now
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# call the function
# print(python_food())  # all functions return something, if nothing specified it returns None
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)  # gives error as len not defined for int, have to convert argument to string
centre_text("spam, spam, spam, and spam")

# print("First", "second", 3, 4, "spam")  # *args, so can put multiple arguments seperated by comma
centre_text("First", "second", 3, 4, "spam", sep=":")
