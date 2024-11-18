# day = "Friday"
# temperature = 30
# raining = False  
# 
# if (day == "Saturday" and temperature > 27) or not raining:  # type: ignore  # if 'and' then Learn Python
#     print("Go swimming")  # 'and' has higher precedence than 'or'
# else:
#     print("Learn Python")

if 0:  # 0 evaluates to false, so else is exe 
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
# if name:  # empty string evaluates to false, so else will be exe
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
