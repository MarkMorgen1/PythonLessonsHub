from datetime import datetime

birthday = datetime(1966, 11, 28, 4, 14, 0)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())
print(datetime(2026, 5, 31).weekday())
print(datetime.now())
delta = datetime(2026, 5, 31) - birthday
print(delta)
