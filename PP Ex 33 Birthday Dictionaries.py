bdays = {"Mark": "11/28/1966", "Joe": "1/2/1988", "Cindy": "8/15/2024"}

print("We have the following names in our list:")
for key in bdays:
    print(key)

request = input("Name of person who's birthday you would like?")
while request not in bdays:
    request = input("Nope.  Try again >>> ")

print("That BDay is: ", bdays[request], "\n")
