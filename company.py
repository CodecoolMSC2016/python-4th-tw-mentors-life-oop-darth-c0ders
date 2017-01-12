from codecool_class import *
from mentor import Mentor
from student import *
import gc
import codecool_class
from tools import Tools
from kitchen import Kitchen
from lounge import Lounge

class Company:

    def apply_for_company():
        applied_students = []
        total_points = 0
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            total_points = student.knowledge_level + student.energy_level
            if total_points >= 60:
                applied_students.append(student)
        print(str(len(applied_students)) + " members applied to company. They are:")
        for student in applied_students:
            print(student.last_name + " " + student.first_name)
                

