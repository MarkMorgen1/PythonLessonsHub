# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
# Extra:
#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string

pwlen = int(input("How many characters would you like in your password? "))
characters = string.ascii_letters + string.digits + "!@#$%^&*()"
print(characters)
password = "".join(random.choice(characters) for i in range(pwlen))
print(password)
