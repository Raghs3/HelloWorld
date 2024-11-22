def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(1): {locals()}')
    # variables defined in enclosing scope become available in inner scopes
    def make_greeting(item: str) -> str:
        print(f'local namespace in `make_greeting(1): {locals()}')
        greeting = 'Hi'  # now greeting doesn't refer to same object as outer function
        print(f'The ID of `greeting` in `make_greeting` id {id(greeting)}')
        print(f'local namespace in `make_greeting(2): {locals()}')
        return f'{greeting} {item}'  # greeting is in enclosing scope but because of free variable it will be found in local
        # greeting also exist in make_greeting namespace (free variables)
    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, `greeting` is {greeting}')
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(2): {locals()}')

# global variable cant be a free variable

names = ['John']  #, 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
# when you bind a free variable to a new value, new variable is created
