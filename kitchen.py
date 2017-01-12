import codecool_class
import random

food_list = [["sport szelet", 2, 5, 1, 2], ["power soup", 10, 12, -2, 5], ["20 days sandwich", -8, -2, -5, -3]]
drink_list = [["beer", -3, 3, -10, -1], ["coffee", 3, 10, 8, 15], ["water", 1, 4, 1, 4]]


class Kitchen:

    @classmethod
    def eating(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            food = random.choice(food_list)
            student.energy_level += random.randint(food[1], food[2])
            student.knowledge_level += random.randint(food[3], food[4])

            print("{0} {1} consumed a(n) \033[94m{2}\033[0m | E: {3}, K: {4}".format(student.last_name,
                                                                                     student.first_name,
                                                                                     food[0],
                                                                                     student.energy_level,
                                                                                     student.knowledge_level))

    @classmethod
    def drinking(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            drink = random.choice(drink_list)
            student.energy_level += random.randint(drink[1], drink[2])
            student.knowledge_level += random.randint(drink[3], drink[4])

            print("{0} {1} consumed a(n) \033[94m{2}\033[0m | E: {3}, K: {4}".format(student.last_name,
                                                                                     student.first_name,
                                                                                     drink[0],
                                                                                     student.energy_level, student.knowledge_level))
