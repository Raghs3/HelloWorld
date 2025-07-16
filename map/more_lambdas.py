anon = lambda x: x * 2  # Not PEP 8 compliant!!!
# lambda for anonymous fn, so no point by naming it


def double(x):
    return x * 2


print(anon)  # function <lambda>
print(lambda x: x * 2)  # same as above
print(double)  # function has a name `double`
