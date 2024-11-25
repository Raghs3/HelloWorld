from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)  # utc is not a timezone but defined like that in timezone class to keep interface consistent
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)

france_tz = zoneinfo.ZoneInfo('Europe/Paris')
france_now = utc_now.astimezone(tz=france_tz)
print(france_now)

print()
print('Available timezone keys')
print('-' * 23)

for zone_key in sorted(zoneinfo.available_timezones()):
    print(zone_key)


# error in importing coz of windows, got to install tzdata module and no need to install zoneinfo (for me)
# my python version is new so already contains zoneinfo
