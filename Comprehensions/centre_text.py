def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"  # minus added to end of string not between items of list
    # text = "-".join(args)  # minus doesn't show now
    text = "-".join([str(arg) for arg in args])  # doesn't give str and int error
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)
    # `str(arg) for arg in args` is not list comprehension as it is not in `[]`, it is a generator expression, but get same output

# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)  # this causes error as can't join int to str
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")
