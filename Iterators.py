letters = ["a", "b", "c"]
new_list = []
for l in letters:  # step through each letter in list letters
    # Appends next letter after making it upper case
    new_list.append(l.upper())
    print(new_list)

# Creates newlist of letters with corresponding positions
newlist = enumerate(letters)
for index, value in newlist:
    print(index, value)

badlist = ["a", "", "c"]  # missing data at second position
# Find position in list of bad data item
newlist = list(enumerate(badlist))
for index, value in newlist:
    print(index, value)
print(newlist)

# Zip three lists together into 3x3 matrix
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
flavors = ["choc", "straw", "peach"]
print(list(zip(letters, numbers, flavors)))
for l, m, n in zip(letters, numbers, flavors):
    print(l, m, n)

# Map function leaves original data in list
print(list(map(str.upper, letters)))
print(letters)
# Convert string values to numberical values
numbers = ["1", "2", "3"]
print(list(map(int, numbers)))

# strip blank spaces from name data
# original list is unchanges
names = ["  John ", "Bill  "]
print(list(map(str.strip, names)))
print(names)

# print out capitalized names line by line
# then strip the blank spaces and print again
capnames = list(map(str.upper, names))
for n in capnames:
    print(n)
capnames_edit = list(map(str.strip, capnames))
for n in capnames_edit:
    print(n)

letters = ["a", False, "b", "c", "", True]
print(letters)
print(list(filter(None, letters)))

# Allow only text strings in list
items = ["sql", "123", "Python", "42"]
print(list(filter(str.isalpha, items)))
for i in filter(str.isalpha, items):
    print(i)
