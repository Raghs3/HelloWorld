from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy1 = copy.deepcopy(original)
copy2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")
jp_list = original["J-P"]  # different ways same activity of changing list
jp_list[1].append("Courier")

print(original)
print(copy1)
print(copy2)
