print("Today is a day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes in strings')
print("hello" + " world")  # no auto spacing in concatenation i.e. joining two strings
greeting = "Hello"
name = "Raghav"  # ask string from user  # input is a fn that assigns inputted value to variable
print(greeting + name)  # no auto spacing

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 14
print(age)

print(type(greeting))  # tells datatype of greeting variable
print((type(age)))  # tells datatype of age variable  # type describes kind of info we are storing

# age = "2 years"  # rebound the label age to str
# or
age_in_words = "2 years"
# print(name + "is" + age + "old")  # type error, can only concatenate str (not int) to str
print(age)
print(type(age))

# f-string

print(name + f" is {age} old")  # using f-string no error (like repfields)

print(f"Pi is approximately {22/7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")
