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


import itertools

party_list = read_guestlist("guest_list.txt")

# Print first 5 guests from file
for name in itertools.islice(party_list, 5):
    print(name)

# Reset generator for dynamic addition
party_list = read_guestlist("guest_list.txt")

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
