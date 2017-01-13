import codecool_class
import random

result_list = ["Won", "Lose"]
playstation_list = [["Grand Theft Auto Hat", -15, -5, -10, -5],
                    ["Super Mario Sisters", -8, -2, -2, 8],
                    ["Postal 2", -4, -2, 0, 8],
                    ["Luna 3D", -8, -2, 0, 8],
                    ["Goat Simulator", -6, -2, 0, 9],
                    ["Need For Weed", -4, -2, 0, 2],
                    ["Earth QUAKE 3", -5, -1, 0, 3],
                    ["Counter-Duty: Modern Offensive", -6, -4, 0, 4],
                    ["FAFI 87.4", -6, -2, 0, 5]]
gym_list = [["Lift Bro", -4, 10, -1, 1],
            ["Helyből távolbanézés", -4, 8, 0, 3],
            ["Run Forrest Run!", -6, 5, 0, 2],
            ["Footballing", 0, 4, 0, 1],
            ["Water poloing", -1, 3, 0, 6],
            ["Bukfencing", -2, 3, 0, 2],
            ["Redbull Drinking", -3, 2, 0, 3],
            ["Boxing", -5, 1, 0, 4]]


class Lounge:

    @classmethod
    def dartsing(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            student.energy_level += random.randint(-2, 2)
            student.knowledge_level += random.randint(0, 4)
            print("{} {} went to play some \033[94mdarts.\033[0m and \033[94m{}\033[0m".format(student.last_name,
                                                                                               student.first_name, random.choice(result_list)))

    @classmethod
    def playstationing(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            playstation = random.choice(playstation_list)
            student.energy_level += random.randint(playstation[1], playstation[2])
            student.knowledge_level += random.randint(playstation[3], playstation[4])

            print("{} {} player a game, called \033[94m{}\033[0m".format(student.last_name,
                                                                         student.first_name,
                                                                         playstation[0]))

    @classmethod
    def gyming(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            gym = random.choice(gym_list)
            student.energy_level += random.randint(gym[1], gym[2])
            student.knowledge_level += random.randint(gym[3], gym[4])

            print("{} {} done \033[94m{}\033[0m to gain some energy.".format(
                student.last_name, student.first_name, gym[0]))

    @classmethod
    def beanbag(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            student.energy_level += random.randint(5, 15)
            student.knowledge_level += random.randint(-1, 1)
        print("Everyone rest some on a beanbag")
