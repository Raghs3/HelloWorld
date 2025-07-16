from data import people, basic_plants_list, plants_list

if all([person[1] for person in people]):  # all people don't have email address
    print("Sending email")

else:
    print("User must edit the list of recipients")
