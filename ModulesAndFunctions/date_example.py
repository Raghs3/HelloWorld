import datetime
import locale

locale.setlocale(locale.LC_ALL, '')  # fr_FR.utf-8 for french # locale functions are not thread safe
# the main program should be responsible for the locale, and imported code should respect that choice, so don't setlocale if you are making a module
start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')  # %A is name of day, %d is day, %B is month name, %Y is year
print(pretty_start)

duration = datetime.timedelta(days=15, hours=48)  # date doesn't have time component so less than 24hrs is lost, units are normalised
end = start + duration
print(end)
print(duration)

d1 = datetime.timedelta(hours=2)
d2 = datetime.timedelta(minutes=120)
d3 = datetime.timedelta(seconds=7200)

print(d1, d2, d3, sep=", ")  # all values are same
print(repr(d1), repr(d2), repr(d3), sep=', ')  # all normalised to seconds, only days, seconds and milliseconds

difference = end - start  # can't add dates
print(repr(difference))
print(difference == duration)



# year = start.year
# month = start.month
# day = start.day
#
# print(f'The {year} winter olympics started on day {day} of month {month}')
#
# today = datetime.date.today()
# print(today)
# print(today.strftime('%A'))
#
# print(today.weekday())  # values are zero-based, monday is 0 not 1
