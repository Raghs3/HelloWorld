for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}"  # {0:2} the 2 is the field width
          .format(i, i ** 2, i ** 3))  # < for left align, > for right align, ^ for center align
    
print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i ** 2, i ** 3))
    
print()

print("Pi is approximately {0:12}".format(22/7))  # general format, defaults to 15 decimals
print("Pi is approximately {0:12f}".format(22/7))  # specifying floating point value using f, default of 6 digits
print("Pi is approximately {0:12.50f}".format(22/7))  # precision of 50, i.e 50 points after decimal point
print("Pi is approximately {0:52.50f}".format(22/7))  # max floating precision is 51-53 digits 
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))  # pads extra with 0s

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {}"
          .format(i, i ** 2, i ** 3))
