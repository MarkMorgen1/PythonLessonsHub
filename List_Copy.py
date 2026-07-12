import copy
original = [
    ['a', 'b'],
    ['c', 'd']
]
# Assignment
copy1 = original
print('Same Object?', original is copy1, "\n")

# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists?", original[0] is copy2[0], "\n")

# Deep Copy -- we want Object and Lists below to be false
# to make sure that we are working with truely seperate data
# Use 'import copy' to import the copy-module into Python,
# then use 'copy.deepcopy(list_name)' to assign to a new list
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists?", original[0] is copy3[0], "\n")

# Combining lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
combined = letters + numbers  # creates longer list, not a matrix
print(combined)
print(letters * 2)
print(letters, numbers)  # creates matrix of lists

# Extend one list with another
print(numbers)
print(letters)
numbers.extend(letters)  # appends letters to numbers list
print(numbers)
print(letters)

# Pair corresponding items in lists. Extras are ignored.
flavors = ['straw','choc', 'vanil']
comb3 = zip(letters, numbers, flavors)
print(comb3)
comb3 = list(zip(letters, numbers, flavors))
print(comb3)
