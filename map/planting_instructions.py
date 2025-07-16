from data import plants_list

with open('planting_instructions.txt', 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        where_to_plant = 'window box' if plant.lifecycle == 'Perennial' else 'garden'
        print(f"{plant.name}: {where_to_plant}", file=output_file)
