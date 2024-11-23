import webbrowser

# webbrowser.open('https://docs.python.org/3.10/library/webbrowser')

chrome = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')  # %s is replaced by the url # (using='google-chrome')  # doesn't work on windows
chrome.open('https://learnprogramming.academy/courses')
