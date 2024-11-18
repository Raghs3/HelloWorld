def removeprefix(string: str, prefix: str) -> str:  # if using before 3.9, use this function
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]  # Return a copy of `string`.


def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):  # suffix=`` should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
# no_apostrophe = first.strip(chars)  # starts removing from one side and stops when it reaches a character not in the string, then other side does same
# print(no_apostrophe)

for character in first:  # how .strip() works
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]:  # process backwards, how strip method works
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

# twas_removed = first.removeprefix("'Twas")  # removes prefix from string
twas_removed = removeprefix(first, "'Twas")  # removes prefix from string
print(twas_removed)
# toves_removed = first.removesuffix('toves')  # removes suffix from string
toves_removed = removesuffix(first, 'toves')  # removes suffix from string
print(toves_removed)
