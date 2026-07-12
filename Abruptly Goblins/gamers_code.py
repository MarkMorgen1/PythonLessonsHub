gamers = []


def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")


kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
print("    LIST OF GAMERS BELOW    ")
print(gamers)
print("-------------  777777777777777  ------------")

add_gamer(
    {"name": "Thomas Nelson", "availability": ["Tuesday", "Thursday", "Saturday"]},
    gamers,
)
add_gamer(
    {
        "name": "Joyce Sellers",
        "availability": ["Monday", "Wednesday", "Friday", "Saturday"],
    },
    gamers,
)
add_gamer(
    {"name": "Michelle Reyes", "availability": ["Wednesday", "Thursday", "Sunday"]},
    gamers,
)
add_gamer({"name": "Stephen Adams", "availability": ["Thursday", "Saturday"]}, gamers)
add_gamer({"name": "Joanne Lynn", "availability": ["Monday", "Thursday"]}, gamers)
add_gamer({"name": "Latasha Bryan", "availability": ["Monday", "Sunday"]}, gamers)
add_gamer(
    {"name": "Crystal Brewer", "availability": ["Thursday", "Friday", "Saturday"]},
    gamers,
)
add_gamer(
    {
        "name": "James Barnes Jr.",
        "availability": ["Tuesday", "Wednesday", "Thursday", "Sunday"],
    },
    gamers,
)
add_gamer(
    {"name": "Michel Trujillo", "availability": ["Monday", "Tuesday", "Wednesday"]},
    gamers,
)
print(" --- List of gamers" * 3)
print(gamers)


def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }


count_availability = build_daily_frequency_table()
print("     BUILD   count_availability\n", count_availability)


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day_name in gamer[
            "availability"
        ]:  # "availability" is a key in the 'gamer' dictionary, and whose values are lists of names of days
            available_frequency[day_name] += 1


calculate_availability(gamers, count_availability)
print("   AVAILABILITY    ------------  \n", count_availability)


def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night


game_night = find_best_night(count_availability)
print("BEST NIGHT IS:", game_night)


def available_on_night(gamers_list, day):
    return [gamer["name"] for gamer in gamers_list if day in gamer["availability"]]


attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer["name"], day_of_week=day, game=game))


send_email(attending_game_night, game_night, "Abruptly Goblins!")
