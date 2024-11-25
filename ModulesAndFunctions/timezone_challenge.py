# Task: display current time in cities: Paris, London, Hong Kong
# Optional: remove fractional seconds and print timezone names (wasn't able to do)

from datetime import datetime, timezone
import zoneinfo

# utc_now = datetime.now(timezone.utc)
#
# paris_tz = zoneinfo.ZoneInfo('Europe/Paris')
# paris_now = utc_now.astimezone(tz=paris_tz)
#
# london_tz = zoneinfo.ZoneInfo('Europe/London')
# london_now = utc_now.astimezone(tz=london_tz)
#
# hongkong_tz = zoneinfo.ZoneInfo('Asia/Hong_Kong')
# hongkong_now = utc_now.astimezone(tz=hongkong_tz)
#
# print(paris_now)
# print(london_now)
# print(hongkong_now)


# TIM SOLN

# Timezone keys for creating the ZoneInfo objects.
zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi',
)

# Get the current time, in UTC
# utc_now = datetime.now(tz=timezone.utc)
local_now = datetime.now()
# local_now = local_now.replace(microsecond=0)

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)  # convert existing time
    # required_time = datetime.now(tz=tz)  # generate new time
    required_time = local_now.astimezone(tz)
    # The city is the last item, after splitting the zone at the /
    city = zone.split('/')[-1]
    print(f'The time in {city} is {required_time} {required_time.tzname()}')
    # print(f'The time in {city} is {required_time.strftime('%d/%m/%Y %H:%M:%S %z %Z')}')

# strftime doesn't modify values
