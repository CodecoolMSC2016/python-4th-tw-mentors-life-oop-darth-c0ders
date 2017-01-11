from codecool_class import *
from mentor import Mentor
from student import *
import gc
import codecool_class
from tools import Tools
from kitchen import Kitchen


def main():
    CodecoolClass.import_mentors()
    CodecoolClass.import_students()
    klassz = CodecoolClass
    klassz.name = input("Give the school name: ")

    student_count = str(len(CodecoolClass.STUDENTS_LIST))
    mentor_count = str(len(CodecoolClass.MENTORS_LIST))
    print("Class {2} created with {0} mentors and {1} students."
          .format(mentor_count, student_count, klassz.name))
    print("Overall energy level at {0} is {1}.".format(klassz.name, CodecoolClass.check_class_energy()))
    for student in codecool_class.CodecoolClass.STUDENTS_LIST:
        Kitchen.eating(student)
        Kitchen.drinking(student)

    Student.stats()


main()
