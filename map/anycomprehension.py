from data import people, basic_plants_list, plants_list

# people = []  # rem the gotcha, all returns true if empty list

if bool(people) and all([person[1] for person in people]):  # all people don't have email address
    print("Sending email")

else:
    print("User must edit the list of recipients")
