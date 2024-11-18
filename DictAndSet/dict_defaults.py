from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)  # setdefault returns value of key if key exists
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)  # beans wasn't in dict so it created beans key and set value to 0
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)  # ketchup doesn't exist in dict
print(f"ketchup: {ketchup_quantity}")  # appears to be same as setdefault but doesnt add the key to the dict like setdefault

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value, sep=": ")
