import sqlite3
import datetime
# import pytz
from SQLite_Converters import adapt_datetime_iso  # , convert_datetime # if writing to the database
# have to use converters wherever database is accessed to makesure str converted to datetime.datetime object.
sqlite3.register_adapter(datetime, adapt_datetime_iso)
# sqlite3.register_converter("datetime", convert_datetime)  # only needed if writing.


# tim old
# db = sqlite3.connect("accounts_iso.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)  # using detect_types makes it so item is datetime.datetime
#
# for row in db.execute("SELECT * FROM history"):  # doing this we realised our time is in str
#     utc_time = row[0]
#     # local_time = utc_time.astimezone()  # why not giving in my timezone!! this is the soln pretty sure ;-;
#     # print(row)
#     local_time = pytz.utc.localize(utc_time).astimezone()  # i'll just use pytz and move on for now ;-;
#     print(f"{utc_time}\t{local_time}")  # time is in string datatype
#
# db.close()  # remember to close the connection!


# my new
db = sqlite3.connect("accounts_iso.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)  # using detect_types makes it so item is datetime.datetime

for row in db.execute("SELECT * FROM history"):  # doing this we realised our time is in str
    utc_time = row[0]
    local_time = utc_time.astimezone()  # why not giving in my timezone!! this is the soln pretty sure ;-;
    # print(row)
    print(f"{utc_time}\t{local_time}")  # time is in string datatype

db.close()  # remember to close the connection!
