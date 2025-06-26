def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


odds = oddnumbers()
