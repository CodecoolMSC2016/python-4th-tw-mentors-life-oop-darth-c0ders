from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import gc
from codecool_class import *


def main():
    CodecoolClass.import_mentors()
    CodecoolClass.import_students()
    klassz = CodecoolClass
    klassz.name = input("Give the school name: ")

    student_count = str(len(STUDENTS_LIST))
    mentor_count = str(len(MENTORS_LIST))
    print("Class {2} created with {0} mentors and {1} students."
          .format(mentor_count, student_count, klassz.name))
    print("Overall energy level at {0} is {1}.".format(klassz.name, CodecoolClass.check_class_energy()))

main()
