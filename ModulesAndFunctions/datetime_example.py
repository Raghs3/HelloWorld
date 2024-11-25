import datetime as dt
from datetime import datetime  # gives error as it replaces entry by line1, as namespace now contains class not module
# if we want to use both imports, gotta use aliasing
today = dt.datetime.today()
now = datetime.now()
# utc_now = datetime.utcnow()  # won't work for me coz its deprecated f
print(today)
print(now)  # both give same value
# print(utc_now)
# better precision with now if C gettimeofday function supported
# now can accept optional tzinfo object
# now is preferred over today
