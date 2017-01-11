from mentor import Mentor
from student import Student
import csv

MENTORS_LIST = []
STUDENTS_LIST = []


class CodecoolClass:

    def __init__(self, name):
        self.name = name

    @classmethod
    def import_mentors(cls):
        with open('./data/mentors.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                temp_mentor = Mentor()
                temp_mentor.first_name = row[0]
                temp_mentor.last_name = row[1]
                temp_mentor.year_of_birth = row[2]
                temp_mentor.gender = row[3]
                temp_mentor.nick_name = row[4]
                MENTORS_LIST.append(temp_mentor)

    @classmethod
    def import_students(cls):
        with open('./data/students.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                temp_student = Student()
                temp_student.first_name = row[0]
                temp_student.last_name = row[1]
                temp_student.year_of_birth = row[2]
                temp_student.gender = row[3]
                temp_student.knowledge_level = row[4]
                temp_student.energy_level = row[5]
                STUDENTS_LIST.append(temp_student)

    def check_class_energy():
        TOTAL_ENERGY = 0
        with open('./data/students.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                temp_student = Student()
                temp_student.first_name = row[0]
                temp_student.last_name = row[1]
                temp_student.year_of_birth = row[2]
                temp_student.gender = row[3]
                temp_student.knowledge_level = row[4]
                temp_student.energy_level = row[5]
                TOTAL_ENERGY += int(temp_student.energy_level)
        return int(TOTAL_ENERGY)
