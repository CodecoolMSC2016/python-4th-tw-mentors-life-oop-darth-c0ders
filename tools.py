import codecool_class
import random


class Tools:
    @classmethod
    def read_book(cls, student):
        student.energy_level += random.randint(-10, 0)
        student.knowledge_level += random.randint(0, 10)
    
    @classmethod
    def do_codewars(cls, student):
        student.energy_level += random.randint(-5, 0)
        student.knowledge_level += random.randint(0, 15)

    @classmethod
    def watch_porn(cls,student):
        student.energy_level += random.randint(5, 10)
        student.knowledge_level += random.randint(-5, 0)

    @classmethod
    def use_google(cls,student):
        student.energy_level += random.randint(-5, 0)
        student.knowledge_level += random.randint(3, 8)

    @classmethod
    def make_presentation(cls,student):
        student.energy_level += random.randint(-12, -6)
        student.knowledge_level += random.randint(2, 8)


