flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
    # 4,  # list must have all str, or it will crash the program
]

# for flower in flowers:
#     print(flower)

separator = ", "
output = separator.join(flowers)  # didin't need to use for loop
print(output)

print(",".join(flowers))
