# create lists
empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = [1, 2, 'a', True, None]

print(empty)  # prints out '[]'
print(type(empty))  # prints '<class 'list'>'

print(letters)  # prints out '['a', 'b', 'c']'
print(type(letters))  # prints '<class 'list'>'

print(numbers)  # prints out '[1, 2, 3]'
print(type(numbers))  # prints '<class 'list'>'

print(mixed)  # prints out '[1, 2, 'a', True, None]'
print(type(mixed))  # prints '<class 'list'>'

letters = list("Data")  # creates list of letters
print(letters)

matrix = [['a', 'b'],
          ['c', 'd']]  # creates a 2D list
print(matrix)
print(type(matrix))

person = ['Bill', 61, 'Billiards Expert', 'Napa']
name, age, talent, city = person
print(talent)
name, *details, city = person
print(details)

numbers = [1, 5, 2, 4, 3, 2]
print("Maximum value is:", max(numbers))
print("Smallest value is:", min(numbers))
print("Sum is:", sum(numbers))
print("# of items:", len(numbers))
print("All Bool value:", all(numbers))
print("0 is a False Bool value in a list:", all([1, 0, 5]))
print("Count of queried value in list: ", numbers.count(2))
print(8 not in numbers)

person = ['Bill', 61, 'Billiards Expert', 'Napa']
nickname = 'Billionaire'
person.insert(1, nickname)
print(person)
removed_item = person.pop(-1)  # remove final item in list and return it
print(person)  # shows list short one item
print(removed_item)  # prints removed item
person.append(removed_item)  # appends removed item to list 'person'
print(person)  # prints 'person' with new items
