import json
import calendar
from collections import Counter

# Note - JSON data does not name the file, so bdays.JSON is not the same data structure as 'bdays' the dictionary within the Python code
# bdays = {"Mark": "11/28/1966", "Joe": "1/2/1988", "Cindy": "8/15/2024"}

# create the JSON file first time using 'bdays' to make sure it exists:
# with open("bdays.json", "w", encoding="utf-8") as f:
#     json.dump(bdays, f, indent=4)

# read the JSON file to get the stored data
with open("bdays.json", "r") as f:
    bdays = json.load(
        f
    )  # redefines the bdays dictionary in Python code from external JSON file

print("JSON Info:", bdays)  # verify the file
# bdays["Sally"] = "3/4/1975"  # for debugging -- add new entry to bdays dictionary in Python

# write updated dict to the JSON file
# with open("bdays.json", "w", encoding="utf-8") as f:
#     json.dump(bdays, f, indent=4)

print("\nEnter the number '1' to add a name")
print("We have the following names in our list:\n")
for key in bdays:
    print(key)
print()

request = input("Name of person who's birthday you would like? (or '1' to add) ")
while request not in bdays and request != "1":
    request = input("Nope.  Try again >>> ")

if request != "1":
    print("That BDay is: ", bdays[request], "\n")
else:  # write new bday to bdays.json file
    new_name = input("Type new name >>> ")
    while new_name in bdays:
        new_name = input("Already in list.  Try another >>> ")
    new_bday = input("Type BDay >>> ")
    bdays[new_name] = new_bday
    print(bdays)
    with open("bdays.json", "w", encoding="utf-8") as f:
        json.dump(bdays, f, indent=4)
    for key in bdays:
        print(key)
    print()

# Using Dictionary Comprehension - {  }
# Keys: 'calendar.month_name[i]' creates the month name from the month value
# Values: 'Counter' counts the number of times each month number occurs
# use .get(i,0) to safely return a 0 if no birthdays in that month
# shows all 12 months
month_counts = {
    calendar.month_name[i]: Counter(
        int(date.split("/")[0]) for date in bdays.values()
    ).get(i, 0)
    for i in range(1, 13)
}
print(month_counts, "\n")


# only prints months with birthdays in chronilogical order
# count occurances of each month using 'Counter()'
month_counter = Counter(int(date.split("/")[0]) for date in bdays.values())
# build dictionary using Dictionary Comprehension
month_counts = {
    calendar.month_name[m]: month_counter[m]
    for m in range(1, 13)
    if month_counter[m] > 0
}
print(month_counts, "\n")
