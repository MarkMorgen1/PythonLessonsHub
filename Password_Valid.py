# Evaluate passwords

email = "fizbo@bestie.com"
password = "21small$X816"
valid_pw = True

username = email.split("@")[0]
print(username)

if password == "":
    print("Password cannot be empty")
    valid_pw = False

if len(password) < 8:
    print("Password must be at least 8 characters long")
    valid_pw = False

if not any(char.isupper() for char in password):
    print("PW must contain at least one UPPER case letter")
    valid_pw = False

if not any(char.islower() for char in password):
    print("PW must contain at least one lower case letter")
    valid_pw = False

if password == email:
    print("PW can not be the same as the email address, Silly")
    valid_pw = False

if " " in password:
    print("PW can not contain any blank spaces")
    valid_pw = False

if not (password[0].isalnum() and password[-1].isalnum()):
    print("PW must begin and end with a letter or a number")
    valid_pw = False

print("Password is valid" if valid_pw else "PW not valid, Silly")
