class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return f"Business Name: {self.name} consists of franchises: {self.franchises}"


class Franchise:
    def __init__(
        self, address, menus
    ):  # 'menus' is a list of the defined Menu objects available at that Franchise 'address', NOT the menus defined as dictionaries later in program
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"Store Address: {self.address}"

    def available_menus(self, time):
        available_menus = []
        for (
            item
        ) in (
            self.menus
        ):  # self.menus is a list of Menu objects from each defined franchise
            if item.start_time <= time <= item.end_time:
                available_menus.append(item)
        return available_menus


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        bill = 0.0
        for item in purchased_items:
            if item in self.items:
                bill += self.items[item]
        return bill


# Create brunch Menu object from brunch dictionary of available items
brunch_dict = {
    "pancakes": 7.50,
    "waffles": 9.00,
    "burger": 11.00,
    "home fries": 4.50,
    "coffee": 1.50,
    "espresso": 3.00,
    "tea": 1.00,
    "mimosa": 10.50,
    "orange juice": 3.50,
}
# the Menu object in this program consists of name of menu + menu dict + start time + end time
brunch_Menu = Menu("Brunch Menu", brunch_dict, 1100, 1600)

# items on Early Bird menu are ordered in a dictionary
early_bird_dict = {
    "salumeria plate": 8.00,
    "salad and breadsticks (serves 2, no refills)": 14.00,
    "pizza with quattro formaggi": 9.00,
    "duck ragu": 17.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 1.50,
    "espresso": 3.00,
}

early_bird_Menu = Menu("Early Bird Menu", early_bird_dict, 1500, 1800)

# Dinner Menu
dinner_dict = {
    "crostini with eggplant caponata": 13.00,
    "caesar salad": 16.00,
    "pizza with quattro formaggi": 11.00,
    "duck ragu": 19.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 2.00,
    "espresso": 3.00,
}
dinner_Menu = Menu("Dinner Menu", dinner_dict, 1700, 2300)

# Kids Menu
kids_dict = {
    "chicken nuggets": 6.50,
    "fusilli with wild mushrooms": 12.00,
    "apple juice": 3.00,
}
kids_Menu = Menu("Kids Menu", kids_dict, 1100, 2100)

print(kids_Menu)
print(brunch_Menu)
print(dinner_Menu)
print("Kids Menu available: ", kids_Menu.start_time, "----", kids_Menu.end_time)

print(brunch_Menu.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird_Menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# Create a list of Menu objects as defined by the Menu class, NOT the dictionaries!  This associates more info with the Menus than just food and price in the dictionaries.
Menus_list = [brunch_Menu, early_bird_Menu, dinner_Menu, kids_Menu]
flagship_Franchise = Franchise("1232 West End Road", Menus_list)
new_Franchise = Franchise("12 East Mulberry Street", Menus_list)
# print(new_Franchise.address)
# print(flagship_Franchise)
# print(kids_menu.start_time)

Basta_Business = Business(
    "Basta Fazoolin' with my Heart", [flagship_Franchise, new_Franchise]
)
print(Basta_Business.franchises)
print("    33333333333333333333     ")

# define Arepa's class objects starting with their dictionary of available items
arepas_dict = {
    "arepa pabellon": 7.00,
    "pernil arepa": 8.50,
    "guayanes arepa": 8.00,
    "jamon arepa": 7.50,
}
print(arepas_dict)
arepas_Menu = Menu("Arepas Menu", arepas_dict, 1000, 2000)
print(arepas_Menu)
arepas_Franchise = Franchise("189 Fitzgerald Avenue", [arepas_Menu])
print(arepas_Franchise)
print("777777777777777777777")
arepas_Business = Business("Take a' Arepa", arepas_Franchise)
print(arepas_Business)
print("-------------------------------")
print(arepas_Franchise.address)
print(arepas_Business.franchises)
print(arepas_Business.franchises.menus[0])
