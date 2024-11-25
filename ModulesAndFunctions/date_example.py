import datetime

start = datetime.date(2022, 2, 4)
print(start)

pretty_start = start.strftime('%A %d %B, %Y')  # %A is name of day, %d is day, %B is month name, %Y is year
print(pretty_start)
