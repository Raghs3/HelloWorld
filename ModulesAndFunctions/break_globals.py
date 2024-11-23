import better_code
from better_code import area_of_square

area = better_code.area_of_square(40)  # area_of_square doesn't exist in global namespace
area = area_of_square(40)  # only namespace is affected in different ways of importing
print(area)

print('Global namespace')
namespace = globals()  # .copy()  # if you don't use copy, error is generated
for name, obj in namespace.items():
    print(name, obj)
