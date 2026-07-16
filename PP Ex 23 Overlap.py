def readfile(filename):
    with open(filename, "r") as temp:
        list_ints = [int(i) for i in temp]  # convert strings to list of integers
        print(list_ints)
        return list_ints


# with open("AA_Happy_Nums.txt") as h:
#     happys = [int(i) for i in h]  # convert strings to list of integers
# print(happys)
# print(h)

# with open("AA_Primes.txt") as p:
#     primes = [int(i) for i in p]  # convert strings to list of integers
# print(primes)

# call readfile() for each text file of numbers
happy_nums = readfile("AA_Happy_Nums.txt")
prime_nums = readfile("AA_Primes.txt")

# convert lists to sets and use '&' or 'intersection', then convert back to a list and sort to put into numerical order.  '&' only works on sets, not lists.
overlap = sorted(list(set(happy_nums) & set(prime_nums)))
print("\nhere is the ordered overlap:\n", overlap)
