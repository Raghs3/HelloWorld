from datetime import time, date

meeting = time(hour = 11, minute = 15, second = 0)
print(meeting)  # exhausted the usefulness of time class

end_time = time(hour=12, minute=30)
print(end_time)
# can't subtract or use timedelta with time class
# can't track date

print(end_time - meeting)  # __sub__ not defined for time class
