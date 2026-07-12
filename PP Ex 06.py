forword = "pacecar"

backword = forword[-1::-1]
print(forword)
print(backword)
if forword == backword:
    print("Lucky palindrome")
else:
    print("Not a palindrome. Fuck off, eh")
