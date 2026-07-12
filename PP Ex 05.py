import itertools
import random

a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 45, 128, 55, 44, 66, 9876, 89, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


def randset(min_length, max_length, low_val, high_val):
    rand_length = random.randint(min_length, max_length)
    random_set = set([random.randint(low_val, high_val) for _ in range(rand_length)])
    print(random_set)
    return random_set


set_a = randset(5, 15, 10, 43)
set_b = randset(5, 15, 10, 43)
print(set_a & set_b)


# c = a & b

# print(c)

# d = set(itertools.chain(a, b))
# print(d)
