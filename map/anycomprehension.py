from data import people, plants_list, plants_dict

# people = []  # rem the gotcha, all returns true if empty list

if bool(people) and all([person[1] for person in people]):  # all people don't have email address
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This dict contains grasses")
else:
    print("No grasses in the dict")

if any(plants_dict[key].plant_type == "Cactus" for key in plants_dict):
    print("This dict contains cacti")
else:
    print("No cacti in the dict")
