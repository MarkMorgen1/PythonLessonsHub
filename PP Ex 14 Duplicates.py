# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.

a_list = [
    1,
    7,
    4,
    99,
    3,
    1,
    "joe",
    "bill",
    "sam",
    "bill",
    "jeff",
]


def dupes_func(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    print(new_list)
    return


def dupes_sets(input_list):
    print(list(set(input_list)))


print(a_list)
dupes_func(a_list)
dupes_sets(a_list)
