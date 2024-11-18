morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# possible_courses = morning ^ afternoon  # XOR operator, gives the difference between the two sets
possible_courses = set(morning).symmetric_difference(afternoon)  # using method we can use list
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)  # using method we can use list
print(possible_courses)
