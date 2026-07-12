class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def set_numberOfStudents(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents

    def __repr__(self):
        return f"We are a {self.level} school named {self.name} with {self.numberOfStudents} students."


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr}\nOur divine pickup policy is {self.pickupPolicy}"


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams_list):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams_list

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        return f"We are {self.name} High School with the following sports: {self.sportsTeams}"


joes_school = PrimarySchool("Joe's School", 55, "Be on Time!")
print(joes_school)
tims_high = HighSchool("Tim's High", 3000, ["Tennis", "bball", "Foot"])
print(tims_high.get_sportsTeams())
print(tims_high)
