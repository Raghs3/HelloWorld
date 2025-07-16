from medals_data import medals_table


def sort_key(d: dict) -> str:
    return d['country']


print(medals_table)
