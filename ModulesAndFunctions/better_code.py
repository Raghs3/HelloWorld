# def area_of_square(length: float):
#     global area
#     area = length * length
#
#
# area_of_square(30)
# print(f'The area is {area}')
# # THIS IS EVEN WORSE


def area_of_square(length: float) -> float:
    return length * length


area = area_of_square(30)
print(f'The area is {area}')
