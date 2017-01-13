from codecool_class import *
from mentor import Mentor
from student import *
import gc
import codecool_class
from tools import Tools
from kitchen import Kitchen
from lounge import Lounge
from company import *
klassz = CodecoolClass


def buildProgram():
    CodecoolClass.import_mentors()
    CodecoolClass.import_students()
    klassz.name = input("Give the school name: ")

    student_count = str(len(CodecoolClass.STUDENTS_LIST))
    mentor_count = str(len(CodecoolClass.MENTORS_LIST))
#\033[94m
