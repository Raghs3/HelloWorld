from medals_data import medals_table


def sort_key(d: dict) -> str:
    return d['rank']


medals_table.sort(key=sort_key)  # cant make it so the fn asks user for field as in sort function cant put params, so lambda useful here
print(medals_table)
