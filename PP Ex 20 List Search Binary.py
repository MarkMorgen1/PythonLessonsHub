# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# a = [1, 3, 5, 7, 15, 74, 88, 105, 111, 121, 133, 144, 155, 166]
# search_val = 111


# high_indx = len(a) - 1
# half_indx = len(a) // 2  # rounds down to integer
# low_indx = 0
# print(low_indx)
# print(half_indx)
# print(high_indx)
# print(a[0])
# print(a[half_indx])
# print(a[high_indx], "\n")

# while (
#     (a[low_indx] < search_val < a[high_indx])
#     and search_val != a[half_indx]
#     and (high_indx - low_indx > 2)
# ):
#     if search_val > a[half_indx]:  # if search_num is in the upper half of list
#         print("Upper Half")
#         print("high index", high_indx)
#         print("half index", half_indx)
#         print("low index", low_indx)
#         print("Value at a[half_indx]", a[half_indx], "\n")

#         # high_indx = high_indx  # keep high_indx same
#         low_indx = half_indx  # redefine low_indx to half-way pt
#         half_indx = (high_indx + low_indx) // 2
#         # define new half_indx between new high and low

#     elif search_val < a[half_indx]:  # if search_num is in the lower half of list
#         print("Lower Half")
#         print("high index", high_indx)
#         print("half index", half_indx)
#         print("low index", low_indx)
#         print("Value at a[half_indx] =", a[half_indx], "\n")

#         high_indx = half_indx  # define new high_indx at halfway pt
#         # low_indx = low_indx # low_indx stays the same
#         half_indx = (high_indx + low_indx) // 2
#         # define new half_indx between new high and low

# print("OUT OF WHILE-LOOP")

# if (
#     search_val != a[low_indx]
#     and search_val != a[half_indx]
#     and search_val != a[high_indx]
# ):
#     print(search_val, "is NOT in your search list")
# elif (
#     search_val == a[low_indx]
#     or search_val == a[half_indx]
#     or search_val == a[high_indx]
# ):  # found it!
#     print(search_val, "is in your search list")

# print("\nEOP")
# print("High Index", high_indx, " = ", a[high_indx])
# print("Half_Index", half_indx, " = ", a[half_indx])
# print("Low_Index", low_indx, " = ", a[low_indx])


# from ChatGPT:
# What I changed
# Simplified variable names: low, high, half instead of low_indx, high_indx, half_indx. Easier to read.
# Single while loop condition: while low <= high is standard for binary search.
# No complicated checks for “difference > 2”.
# Recalculate half once per loop after adjusting low or high.
# Final check uses else: on the while loop—executed only if break never occurs.
# Debug prints remain so you can see which half is being checked and index updates.
# Ordered list and search value
a = [1, 3, 5, 7, 15, 74, 88, 105, 111, 121, 133, 144, 155, 166]
search_val = 3

# Initialize indices
low = 0
high = len(a) - 1

# Initial half index
half = (low + high) // 2

print("Initial indices:")
print("Low:", low, "=", a[low])
print("Half:", half, "=", a[half])
print("High:", high, "=", a[high], "\n")

# Binary search loop
while low <= high:
    print(f"Checking a[{half}] = {a[half]}")

    if a[half] == search_val:
        print(f"Found {search_val} at index {half}")
        break
    elif a[half] < search_val:
        print("Going to upper half\n")
        low = half + 1  # move low up by one since a[half] already checked
    else:  # a[half] > search_val
        print("Going to lower half\n")
        high = half - 1  # move high down by one

    half = (low + high) // 2  # recalc middle

else:  # executed if while loop exits normally (not break)
    print(f"{search_val} is NOT in the list")

print("\nFinal indices:")
print("Low:", low, "=", a[low] if low < len(a) else "out of range")
print("Half:", half, "=", a[half] if 0 <= half < len(a) else "out of range")
print("High:", high, "=", a[high] if high >= 0 else "out of range")
