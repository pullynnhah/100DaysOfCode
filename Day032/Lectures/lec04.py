import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))
print()

year = now.year
weekday = now.weekday()
print(year)
print(weekday)
print()

date_of_birth = dt.datetime(year=1996, month=6, day=21, hour=7, minute=20)
print(date_of_birth)
