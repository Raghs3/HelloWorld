def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    # variables defined in enclosing scope become available in inner scopes
    def make_greeting(item: str) -> str:
        return f'{greeting} {item}'  # greeting is in enclosing scope but because of free variable it will be found in local
        # greeting also exist in make_greeting namespace (free variables)
    for item in items:
        print(make_greeting(item))
# global variable cant be a free variable

names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
