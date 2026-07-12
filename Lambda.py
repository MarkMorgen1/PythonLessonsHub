# Lambda function definitions
# output = lambda x: f(x)
multi = lambda x: x * 2
print(multi(3.5))

addup = lambda x, y: x + y
print(addup(3, 8))

textstr = "Python"
checker = lambda i: i in textstr  # returns boolean
print(checker("a"))  # call "i in textstr" for letter'a', return boolean

# Map + lambda - convert list of string prices to float
prices = ["$12.50", "$9.99", "$100.00"]
# start with single value then work to the list
p1 = "$7.50"
# convert p1 to float and verify type before working on list
print(type(float(p1.replace("$", ""))))
# do same thing for the list prices
# First define the function 'convert_to_float'
convert_to_float = lambda p: float(p.replace("$", ""))
print(type(convert_to_float))
float_vals = list(map(convert_to_float, prices))
print(f"Converted values: {float_vals}")

# Filter out values < 100 from numbers list
numbers = [75, 100, 34, 150]
nums_func = lambda n: n >= 100
print("Nums_func is of type", type(nums_func))
print(list(filter(nums_func, numbers)))  # only keeps values >= 100
print(len(list(filter(nums_func, numbers))))

# Filter out names who have scores < some value
min_score = 80
students = [["Mark", 92], ["Cindy", 85], ["Moe", 78]]
# Individually verify True and False conditions based on score
print(students[1][1] > min_score)
# Input each row as the argument in lambda definition
# and keep all names and scores > min_score
# MATRIX ITERATION ALWAYS WORKS ONE ROW AT A TIME, SO ONLY THE COLUMN
# NUMBER OF THE SCORE NEEDS TO BE DEFINED
chk_score_func = lambda row: row[1] > min_score  # define func chk_score_func
filter_score = filter(chk_score_func, students)  # filter(action, iterable)
print(list(filter_score))  # convert filtered data to list and print it
# shortcut version:
print(list(filter(lambda row: row[1] > min_score, students)))

# TASK: keep names and scores of student names that start with M
students = [["Mark", 92], ["Cindy", 85], ["Moe", 78]]
# first, test code on single item in list to make sure it works
print(students[1][0])
if students[1][0].startswith("M"):
    print("YES")
else:
    print("Nope")

m_names = list(filter(lambda row: row[0].startswith("M"), students))
print(m_names)
