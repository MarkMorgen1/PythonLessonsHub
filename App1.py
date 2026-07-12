import math
import random
course = "Python Programming"
# print(len(course))
print(course.upper())
print(math.log(1/2))
# x = input("Enter x ")
# y = int(x) + 1
# print(f"y =", y)
# print(f"x = {x}")
count = 0
for num in range(1, 10):
    if (num % 2) == 0:
        print(num)
        # count = count + 1
        count += 1
print(f"we have {count} even numbers")

info = 'Tom-24-Spain'
new_list = info.split("-")
print(new_list)
print(sorted(new_list))

textstr = "968-JayZ, ( D@t@ Engineer );; 27y  "
print(textstr)
print(len(textstr))
textstr = textstr.strip().lower()
print(len(textstr))
textstr = textstr.strip('968-')
first_name = textstr[0:4]
print(first_name)

textstr = textstr.strip('JayZ,')
textstr = textstr.strip()
textstr = textstr.replace('@', 'a')
textstr = textstr.replace('(', '').strip()

role = textstr[:13]
print(role)

age = textstr[-3:-1]
print(age)

print(f"name: {first_name} | role: {role} | age: {age}")

rdm = random.randint(1, 100)
print(rdm)
evenchk = rdm % 2
if evenchk == 0:
    print(f"{rdm} is an even number")
else:
    print(f"{rdm} is an odd number")

username = "Billy Kid"
age = 35
email = "cheese@ball.com"
password = "Apple 12345"
print((username != None) and age >= 18)
if (len(password) > 8 and (" " not in password)):
    print("Password is OK")
else:
    print("Issue with pw")
print(email != None and ("@" in email) and (email.endswith(".com")))
if ((type(username) == str) and (username != None) and (len(username) > 5)):
    print("Username is valid")
else:
    print("Problem with username")

for i in range(1, 3+1):
    print(f"Loop # {i}")


def greet(name):
    print(f"Hello, {name}")


greet("sammy")
greet("Joe")
greet(username)
if age == 35:
    print(f"Age is {age}")

email = "5toolbox@silly.org"
user = email.split("@")  # creates list of two strings
user = user[0]
print(user)

if (email != None) and ("." in email) and ("@" in email) and (email.count("@") == 1) and (" " not in email) and (email.endswith(".com") or email.endswith(".org")) and (len(email) <= 254) and (user[0].isalpha() or user[0].isdigit) and (user[-1].isalpha() or user[-1].isdigit):
    print("email format is valid")
else:
    print("Problem with email address")
print(user[-1].isalpha())
print(user[-1])
print(user[0].isalpha())
print(user[0])
