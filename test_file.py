guests = {}


def read_guestlist(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue
        name, age = parts
        age = int(age)
        guests[name] = (
            age  # this line adds both 'name' and 'age' to the guests dictionary
        )

        # Yield the name and simultaneously capture a .send() value
        n = yield name
        # If a new guest is sent in using .send() in body of program, handle immediately
        while n is not None:
            parts = n.strip().split(",")
            if len(parts) == 2:
                new_name, new_age = parts
                new_age = int(new_age)
                guests[new_name] = new_age
                # Yield new guest and wait for next send()
                n = yield new_name
            else:
                n = None  # ignore malformed input


# -----------------------------------------
def table_1():
    for seat_num in range(1, 6):
        yield ("Chicken ", "Table_1 ", "Seat " + str(seat_num))


def table_2():
    for seat_num in range(1, 6):
        yield ("Beef ", "Table_2 ", "Seat " + str(seat_num))


def table_3():
    for seat_num in range(1, 6):
        yield ("Fish", "Table_3", "Seat " + str(seat_num))


# ------------------------------------------------
def assign_seats(seating_generator):
    for guest in guests:
        try:
            yield (guest, next(seating_generator))
        except StopIteration:
            # Seating generator exhausted
            print("No more seats available!")
            break


# -------------------------------------------

import itertools

party_list = read_guestlist(
    r"C:\Users\markm\OneDrive\Desktop\Python files\guest_list.txt"
)  # use 'r' before path to tell Python that back-slashes are literal, not coded escape characters
# Print first 5 guests from file
for name in itertools.islice(party_list, 5):
    print(name)

# Reset generator for dynamic addition
party_list = read_guestlist(
    r"C:\Users\markm\OneDrive\Desktop\Python files\guest_list.txt"
)
# Prime the generator to first yield
print(next(party_list))  # prints first file guest
# Dynamically add Jane
print(party_list.send("Jane,35"))  # prints Jane immediately
# Continue printing next 5 guests
for _ in range(5):
    print(next(party_list))
# Print remaining guests
for guest in party_list:
    print(guest)

# Print full dictionary
print("\nGuests dict:")
print(guests)

# generator of names 21 and over
adult_guests = (name for name, age in guests.items() if age >= 21)
for adult in adult_guests:
    print(adult)
kid_guests = (name for name, age in guests.items() if age < 21)
for kid in kid_guests:
    print("Under 21: ", kid)

t1 = table_1()
for t in t1:
    print(t)

t2 = table_2()
for t in t2:
    print(t)

t3 = table_3()
for t in t3:
    print(t)

# recreate exhausted tables
t1 = table_1()
t2 = table_2()
t3 = table_3()
all_tables = itertools.chain(t1, t2, t3)

seats = assign_seats(all_tables)
for seat in seats:
    print(seat)
