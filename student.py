from person import Person
import codecool_class


class Student(Person):

    def __init__(self):
        self.knowledge_level = 0
        self.energy_level = 0

    def stats():
        total_points = 0
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            total_points += student.knowledge_level + student.energy_level
            #print(student.last_name + " " + student.first_name + " has " + str(student.knowledge_level) + " knowledge level and " + str(student.energy_level) + " energy level.")
            print(student.last_name + " " + student.first_name + " has " + str(total_points) + " points.")
            total_points = 0

