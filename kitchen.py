import codecool_class
import random


class Kitchen:
    @classmethod
    def eat_sport_szelet(cls, student):
        student.energy_level += random.randint(2, 5)
        student.knowledge_level += random.randint(1, 2)

    @classmethod
    def eat_power_soup(cls, student):
        student.energy_level += random.randint(10, 12)
        student.knowledge_level += random.randint(-2, 5)

    @classmethod
    def eat_20_days_sandwich(cls, student):
        student.energy_level += random.randint(-8, -2)
        student.knowledge_level += random.randint(-5, -3)

    @classmethod
    def drink_beer(cls, student):
        student.energy_level += random.randint(-3, 3)
        student.knowledge_level += random.randint(-1, -10)

    @classmethod
    def drink_coffee(cls, student):
        student.energy_level += random.randint(3, 10)
        student.knowledge_level += random.randint(8, 15)
    
    @classmethod
    def drink_water(cls, student):
        student.energy_level += random.randint(1, 4)
        student.knowledge_level += random.randint(1, 4)