available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "HDMI Cable",
                   "6": "DVD Drive",
                   }

computer_parts = []
current_choice = None

while current_choice != "0":
    if current_choice in available_parts:  # checking keys
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")

print(computer_parts)
