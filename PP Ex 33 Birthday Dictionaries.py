import json

# Note - JSON data does not name the file, so bdays.JSON is not the same data structure as 'bdays' the dictionary within the Python code
bdays = {"Mark": "11/28/1966", "Joe": "1/2/1988", "Cindy": "8/15/2024"}

# create the JSON file first time using 'bdays' to make sure it exists:
# with open("bdays.json", "w", encoding="utf-8") as f:
#     json.dump(bdays, f, indent=4)

# read the JSON file to get the data
with open("bdays.json", "r") as f:
    bdays = json.load(f)  # redefines the bdays dictionary from JSON file

print("JSON Info:", bdays)  # verify the file
bdays["Sally"] = "3/4/1975"  # add new entry to bdays dictionary in Python

# write updated dict to the JSON file
with open("bdays.json", "w", encoding="utf-8") as f:
    json.dump(bdays, f, indent=4)

print("Enter the number '1' to add a name")
print("We have the following names in our list:")
for key in bdays:
    print(key)
print()

request = input("Name of person who's birthday you would like? (or '1' to add) ")
while request not in bdays and request != "1":
    request = input("Nope.  Try again >>> ")

if request != "1":
    print("That BDay is: ", bdays[request], "\n")
else:
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
