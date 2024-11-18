# jabber = open('Jabberwocky.txt', 'r')  # not best way to open file
#
# for line in jabber:
#     # print(line, end='')
#     # print(line.strip(), end='')  # strip() removes leading and trailing white space, it includes new line character (\n)
#     # print(line.strip())
#     print(line.rstrip())  # rstrip() remove trailing white space from right (end of str)
#     # print(len(line))
#
# jabber.close()

# with open('Jabberwocky.txt', 'r') as jabber:  # closes file automatically when loop ends
#     # for line in jabber:  # `with` is statement so no return value
#     #     print(line.rstrip())
#     lines = jabber.readlines()  # returns list of strings for each line in file
#
# print(lines)  # we can see the new line characters
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end='')

# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()  # reads entire file into a single string
#
# # print(text)
# for character in reversed(text):
#     print(character, end='')

# with open('Jabberwocky.txt') as jabber:
#     while True:
#         line = jabber.readline().rstrip()  # this method if we want to further process string
#         print(line)
#         if 'jubjub' in line.casefold():
#             break
#
# print('*' * 80)


with open('Jabberwocky.txt', encoding='utf-8') as jabber:  # same as above
    for line in jabber:
        print(line.rstrip())  # does not store line in variable
