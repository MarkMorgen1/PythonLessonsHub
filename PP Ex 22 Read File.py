# a = []

# with open("guest_list.txt", "r") as read_file:
#     line = read_file.readline()

#     while line:
#         line = line.strip()  # remove \n and spaces from start/end
#         print(line)
#         a.append(line)
#         line = read_file.readline()

# print("---------------------------")
# print(a)

a = []  # define the list to read lines of text into

# open the file 'guest_list.txt' in read mode into 'read_file' object
with open("guest_list.txt", "r", encoding="utf-8") as read_file:
    a = [each_line.strip() for each_line in read_file]  # i.e. for-loop

print("Final list a:", a)

# eliminate duplicates in list a, place into list a_short
a_short = []
for name in a:
    if name not in a_short:
        a_short.append(name)

# use list comprehension to eliminate duplicates
# b_short = []
# b_short = [item for index, item in enumerate(a) if item not in a[:index]]

print("\na-Short List:", a_short, "\n")

# Count occurences of each name in 'a' using for-loop
name_count = {}
for each_name in a_short:
    name_count[each_name] = a.count(each_name)  # add key:item to set
print(name_count, "\n")

# Count occurrences in 'a' using dictionary comprehension
name_counts = {
    name: a.count(name) for name in set(a)
}  # add key:value into set name_counts in form name:count.  'a' is converted to a set to remove duplicate occurences in the 'a' list
print(name_counts)

# Sample
# g = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]
# print(g.count("Alice"))  # 3
# print(g.count("Bob"))  # 2
# print(g.count("Eve"))  # 1
# print(g.count("Charlie"))  # 0
