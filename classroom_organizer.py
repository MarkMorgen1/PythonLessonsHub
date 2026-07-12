import roster
import itertools


# Import modules above this line
class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(roster.student_roster)
        self.index = 0  # <-- required by the exercise

    # def __iter__(self):  # See new code below
    #     self.index = 0
    #     return self

    # def __next__(self):
    #     if self.index >= len(self.sorted_names):
    #         raise StopIteration
    #     name = self.sorted_names[self.index]
    #     self.index += 1
    #     return name

    def roll_call(self):  # this method replaces '__iter__' & '__next__' above
        for name in self.sorted_names:
            yield name  # returns one name per call to method without storing the entire list in memory. Use a for-loop to get all names one at a time.  See file 3File_Class_iter_script.py for call

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info["name"]
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in roster.student_roster:
            if student["favorite_subject"] == subject:
                selected_students.append((student["name"], subject))
        return selected_students

    def table_combos(self):
        return list(itertools.combinations(self.sorted_names, 2))

    def math_and_science(self):
        math_list = self.get_students_with_subject("Math")
        sci_list = self.get_students_with_subject("Science")
        combined = itertools.chain(math_list, sci_list)
        return list(itertools.combinations(combined, 4))
