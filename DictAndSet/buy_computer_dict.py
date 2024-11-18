available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "HDMI Cable",
                   "6": "DVD Drive",
                   }

current_choice = None
computer_parts = {}  # create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:  # checking keys
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(chosen_part))
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
