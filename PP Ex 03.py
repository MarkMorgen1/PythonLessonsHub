a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

num = int(input("enter your number: "))

[b.append(i) for i in a if i <= num]

print(b)
