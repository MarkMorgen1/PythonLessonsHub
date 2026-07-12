# check for factors or prime-ness

num = int(input("  Enter an integer > 1; 0 or 1 to exit: "))
while num > 1:
    b = []
    nums_list = range(2, num // 2 + 2)
    print(list(nums_list))
    [
        b.append(i) for i in nums_list if num % i == 0
    ]  # fill list b with all factors of num
    if len(b) == 0:
        print(" ", num, "is prime")
    else:
        print("  Factors of your number are:", b)
    num = int(input("  Enter an integer > 1; 0 or 1 to exit: "))
