import codecool_class
import random

playstation_list =[["play_mortal_kombat", -15, -5, -10, -5],["play_fifa", -8, -2, -2, 8]]
gym_list = [["do_gimnastics", -5, 10, 0, 0],["run", -3, 8, 0, 1]]

class Lounge:

    @classmethod
    def dartsing(cls, student):
        student.energy_level += random.randint(-2, 2)
        student.knowledge_level += random.randint(0, 4)

    @classmethod
    def playstationing(cls, obj):
        playstation = random.choice(playstation_list)
        obj.energy_level += random.randint(playstation[1],playstation[2])
        obj.knowledge_level += random.randint(playstation[3],playstation[4])

    @classmethod
    def gyming(cls, obj):
        gym = random.choice(gym_list)
        obj.energy_level += random.randint(gym[1],gym[2])
        obj.knowledge_level += random.randint(gym[3],gym[4])

    @classmethod
    def beanbag(cls, student):
        student.energy_level += random.randint(5, 15)
        student.knowledge_level += random.randint(-1, 1)
    


