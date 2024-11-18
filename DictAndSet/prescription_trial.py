from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # if warfarin in prescription:  # slow as testing takes time
    #     prescription.remove(warfarin)
    #     prescription.add(edoxaban)
    # else:
    try:
        # prescription.discard(warfarin)  # doesnt give error so doesn't work and kills Kenny
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial")
    print(patient, prescription)
