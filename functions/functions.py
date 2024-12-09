def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)
    # print("spam and eggs")


def centre_text(*args, sep=' '):
    # text = str(text)
    text = ""
    for arg in args:
        text += str(arg) + sep
    # text = text.rstrip(sep)  # if we want to remove the trailing colon, but will be solved using comprehensions so no need to do right now
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text


# with open("centred", mode='w') as centred_file:

# call the function
# print(python_food())  # all functions return something, if nothing specified it returns None
# s1 = centre_text("spam and eggs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text(12)  # gives error as len not defined for int, have to convert argument to string
# print(s3)
# s4 = centre_text("spam, spam, spam, and spam")
# print(s4)
#
# # print("First", "second", 3, 4, "spam")  # *args, so can put multiple arguments seperated by comma
# s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
# print(s5)  # directly call inside print or use variable, both works when a function returns something


with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("spam, spam, spam, and spam"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)
