# FOR Loops
for i in range(2, 11, 2):
    print(f"number {i}")

product = 1
for i in range(1, 3):
    product = 7 * i
    print(f"7 x {i} = {product}")

for n in range(1, 4):
    print("*" * n)

product = 1
for i in range(1, 4):
    for j in range(3, 5):
        product = i*j
        print(f"{i} x {j} = {product}")

emails = [
    'data@gmail.com',
    'bookdate@outlook.de',
    'DROP TABLE OF USERS;',
    'cindy@gmail.com'
]
for email in emails:
    if ";" in email:
        print('SQL Injection: potential hack. Stopping process.')
        break  # gets out of loop if emails list contains bad data
    print(f'processing email: {email}')
else:
    print('All data is ok')

items = [1, 3, 4, 5, 7]
for item in items:
    if item % 2 == 0:  # check for even number
        print(f'even # found: {item}')
        break  # gets out of loop if an even number is found
else:
    print('All numbers are odd')

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'report.csv',
    'data.csv'
]

dup_list = file_list
count = 0
for file_name in file_list:
    for dup_name in dup_list:
        if file_name == dup_name:
            count = count + 1
if count > len(file_list):
    print(f"Multiple occurances of same file name found in {file_list}")
    for file_name in file_list:
        if file_list.count(file_name) > 1:
            print(file_name)
    print(count)
else:
    print('No duplicates')
    print(count)

# WHILE Loops
# answer = 'no'
# while answer != "yes":
#    answer = input("Do you agree (yes / no): ")
# print("Thank you")

count = 0
while count < 3:
    answer = input("Do you agree? (yes / no): ")
    if answer == "yes":
        print("We are all in agreement")
        break
    count += 1
else:
    print("3 Strikes, Beavis!")
