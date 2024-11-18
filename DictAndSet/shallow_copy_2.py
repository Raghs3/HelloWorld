lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals ={
    "lion": lion_list,  # accurate reflection of how dict actually stored
    "elephant": elephant_list,
    "teddy": teddy_list,
}

# things = animals.copy()  # shallow copy, still only 3 lists not 6
things = {  # both dict referring to same lists
    "lion": lion_list,
    "elephant": elephant_list,  # shallow copy copies the references not the items it refers to
    "teddy": teddy_list,
}

print(things["teddy"])
print(animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")  # same as above
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)
