b = []
num = int(input("enter your number: "))
nums_list = range(2, num)
# for i in nums_list:
#     if num % i == 0:
#         b.append(i)

[b.append(i) for i in nums_list if num % i == 0]  # fill list b with
print(b)
