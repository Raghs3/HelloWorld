from datetime import time, date

meeting = time(hour = 11, minute = 15, second = 0)
print(meeting)  # exhausted the usefulness of time class

end_time = time(hour=12, minute=30)
print(end_time)
# can't subtract or use timedelta with time class
# can't track date

# print(end_time - meeting)  # __sub__ not defined for time class

iso_time = 'T11:15:00'  # in older version of python, adding `T` gives error
_time = time.fromisoformat(iso_time)  # used underscore to avoid conflict with time class
print(_time)

iso_date = '2022-05-10'
_date = date.fromisoformat(iso_date)
print(_date)
