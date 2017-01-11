import codecool_class
import random

laptop_list = [["do_codewars", -5, 0, 0, 15],["watch_porn", 5, 10, -5, 0],["use_google", -5, 0, 3, 8]]

class Tools:
    @classmethod
    def read_book(cls, student):
        student.energy_level += random.randint(-10, 0)
        student.knowledge_level += random.randint(0, 10)
    
    @classmethod
    def laptoping(cls, obj):
        laptop = random.choice(laptop_list)
        obj.energy_level += random.randint(laptop[1],laptop[2])
        obj.knowledge_level += random.randint(laptop[3],laptop[4])
        
        print("{0} consumed a(n) {1}".format(obj.last_name + obj.first_name, laptop[0]))

    @classmethod
    def make_presentation(cls,student):
        student.energy_level += random.randint(-12, -6)
        student.knowledge_level += random.randint(2, 8)


