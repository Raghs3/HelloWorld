from collections import namedtuple

people = [
    ("John Cleese", "cleese@gmail.com"),
    ("Terry Gilliam", "gilliam@gmail.com"),
    ("Eric Idle", ""),
    ("Terry Jones", "jones@gmail.com"),
    ("Graham Chapman", "chapman@gmail.com"),
    ("Michael Palin", "")
]

# Named Tuples are described in the documentation
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# field_names can't start with underscore
# Plant = namedtuple('Plant', ['name', 'scientific_name', 'lifecycle', 'plant_type'])  # change to P to see how it affects then undo changes
Plant = namedtuple('Plant', 'name, scientific_name, lifecycle, plant_type')  # can give comma separated names in string as well
PlantDetails = namedtuple('PlantDetails', ['scientific_name', 'lifecycle', 'plant_type'])  # the typename is printed when printing the named tuple
# variable name and typename same to avoid confusion
basic_plants_list = [
    ("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
    ("Bellflower", "Campanula", "perennial", "Flower"),
    ("China Pink", "Dianthus", "Perennial", "Flower"),
    ("Daffodil", "Narcissus", "Perennial", "Flower"),
    ("Evening Primrose", "Oenothera", "Biennial", "Flower"),
    ("French Marigold", "Tagetes patula", "Annual", "Flower"),
    ("Golden Hakone Grass", "Hakonechloa macra", "Perennial", "Grass"),
    ("Hydrangea", "Hydrangea", "evergreen", "Shrub"),
    ("Iris", "Iris", "Perennial", "Flower"),
    ("Japanese Camellia", "Camellia japonica", "Evergreen", "Shrub"),
    ("Lavender", "Lavendula", "Perennial", "Plant/shrub"),
    ("Lilac", "Syringa vulgaris", "Deciduous", "Shrub"),
    ("Magnolia", "Magnolia", "Deciduous, evergreen", "Shrub"),
    ("Peony", "Paeonia", "Perennial", "Shrub"),
    ("Queen Anne's Lace", "Daucus carota", "Biennial", "Flower"),
    ("Red Hot Poker", "Kniphofia", "Perennial", "Flower"),
    ("Snapdragon", "Antirrhinum majus", "Annual", "Flower"),
    ("Sunflower", "Helianthus", "Annual", "Flower"),
    ("Tiger Lily", "Lilinium tigrinium", "Perennial", "Flower"),
    ("Witch Hazel", "Hamamelis", "Deciduous", "Shrubs"),
]

plants_list = [
    Plant("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
    Plant("Bellflower", "Campanula", "Perennial", "Flower"),
    Plant("China Pink", "Dianthus", "Perennial", "Flower"),
    Plant("Daffodil", "Narcissus", "Perennial", "Flower"),
    Plant("Evening Primrose", "Oenothera", "Biennial", "Flower"),
    Plant("French Marigold", "Tagetes patula", "Annual", "Flower"),
    Plant("Golden Hakone Grass", "Hakonechloa macra", "Perennial", "Grass"),
    Plant("Hydrangea", "Hydrangea", "evergreen", "Shrub"),
    Plant("Iris", "Iris", "Perennial", "Flower"),
    Plant("Japanese Camellia", "Camellia japonica", "Evergreen", "Shrub"),
    Plant("Lavender", "Lavendula", "Perennial", "Shrub"),
    Plant("Lilac", "Syringa vulgaris", "Deciduous", "Shrub"),
    Plant("Magnolia", "Magnolia", "Deciduous, evergreen", "Shrub"),
    Plant("Peony", "Paeonia", "Perennial", "Shrub"),
    Plant("Queen Anne's Lace", "Daucus carota", "Biennial", "Flower"),
    Plant("Red Hot Poker", "Kniphofia", "Perennial", "Flower"),
    Plant("Snapdragon", "Antirrhinum majus", "Annual", "Flower"),
    Plant("Sunflower", "Helianthus", "Annual", "Flower"),
    Plant("Tiger Lily", "Lilinium tigrinium", "Perennial", "Flower"),
    Plant("Witch Hazel", "Hamamelis", "Deciduous", "Shrub"),
]

plants_dict = {
    "Andromeda": PlantDetails("Pieris japonica", "Evergreen", "Shrub"),
    "Bellflower": PlantDetails("Campanula", "Annual, biennial, perennial", "Flower"),
    "China Pink": PlantDetails("Dianthus", "Perennial", "Flower"),
    "Daffodil": PlantDetails("Narcissus", "Perennial", "Flower"),
    "Evening Primrose": PlantDetails("Oenothera", "Biennial", "Flower"),
    "French Marigold": PlantDetails("Tagetes patula", "Annual", "Flower"),
    "Golden Hakone Grass": PlantDetails("Hakonechloa macra", "Perennial", "Grass"),
    "Hydrangea": PlantDetails("Hydrangea", "Deciduous, evergreen", "Shrub"),
    "Iris": PlantDetails("Iris", "Perennial", "Flower"),
    "Japanese Camellia": PlantDetails("Camellia japonica", "Evergreen", "Shrub"),
    "Lavender": PlantDetails("Lavendula", "Perennial", "Shrub"),
    "Lilac": PlantDetails("Syringa vulgaris", "Deciduous", "Shrub"),
    "Magnolia": PlantDetails("Magnolia", "Deciduous, evergreen", "Shrub"),
    "Peony": PlantDetails("Paeonia", "Perennial", "Shrub"),
    "Queen Anne's Lace": PlantDetails("Daucus carota", "Biennial", "Flower"),
    "Red Hot Poker": PlantDetails("Kniphofia", "Perennial", "Flower"),
    "Snapdragon": PlantDetails("Antirrhinum majus", "Annual", "Flower"),
    "Sunflower": PlantDetails("Helianthus", "Annual", "Flower"),
    "Tiger Lily": PlantDetails("Lilinium tigrinium", "Perennial", "Flower"),
    "Witch Hazel": PlantDetails("Hamamelis", "Deciduous", "Shrub"),
}
