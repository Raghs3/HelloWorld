def greet_pythons(items: list) -> None:
    greeting = 'Hello'

    def make_greeting(item: str) -> str:
        return f'{greeting} {item}'  # greeting is enclosing scope?

    for item in items:
        print(make_greeting(item))


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
