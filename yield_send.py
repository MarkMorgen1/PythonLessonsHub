MAX_STUDENTS = 50


def get_student_ids():
    student_id = 1
    while student_id <= MAX_STUDENTS:
        # Write your code below
        n = yield student_id
        if n is not None:
            student_id = n
            continue
        student_id += 1


student_id_generator = get_student_ids()
for i in student_id_generator:
    # Write your code below
    if i == 7:  # after 6 id's have been assigned...
        i = student_id_generator.send(
            45
        )  # ... start ids at .send(value) by internally assigning n = value at 'yield' in code above.  new n is first used in code at 'if n is not None', NOT at n = yield student_id because code is executed left to right
    print(i)
