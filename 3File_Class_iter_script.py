import roster
import classroom_organizer
import itertools

stud_dicts_iter = iter(roster.student_roster)
print(next(stud_dicts_iter))

print("________________________________________")

my_organizer = classroom_organizer.ClassroomOrganizer()

print("-------  Tables-of-2 Combos   --------")
print(my_organizer.table_combos())
print(len(my_organizer.table_combos()))
print()
print("--------  Math Tables  -----")
print(my_organizer.math_and_science())
print(len(my_organizer.math_and_science()))

print(my_organizer.math_and_science()[0])
print(my_organizer.math_and_science()[0][0])
print(my_organizer.math_and_science()[0][0][0])

for nameA in my_organizer.roll_call():
    print("---", nameA)

for nameB in my_organizer.roll_call():
    print(nameB)
print("BBBBBBBBBBBBBBBBBBBBBBBBBBBB")

for stud in my_organizer.roll_call():  # prints entire list of students
    print(stud)
print("CCCCCCCCCCCCCCCCCCCCCCCCCCCC")

roll_iterator = my_organizer.roll_call()  # define generator object
print(next(roll_iterator))  # first student
print(next(roll_iterator))  # second student
print(next(roll_iterator))  # third student
print(next(roll_iterator))
print(next(roll_iterator))
print("  ENOUGH    ENOUGH  ENOUGH ")

roll_iterator = (
    my_organizer.roll_call()
)  # restarts roll_call at beginning of list following prior 'next' statements
while True:
    try:
        name = next(roll_iterator)
        print(name)
    except StopIteration:
        break
