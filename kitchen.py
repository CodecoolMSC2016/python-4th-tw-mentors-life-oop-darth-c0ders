import codecool_class
import random

food_list = [["sport szelet", 2, 5, 1, 2],["power soup", 10, 12, -2, 5],["20 days sandwich", -8, -2, -5, -3]]
drink_list = [["beer", -3, 3, -10, -1],["coffee", 3, 10, 8, 15],["water", 1, 4, 1, 4]]

class Kitchen:



    @classmethod
    def eating(cls, obj):
        food = random.choice(food_list)
        obj.energy_level += random.randint(food[1],food[2])
        obj.knowledge_level += random.randint(food[3],food[4])
        
        print("{0} consumed a(n) {1}".format(obj.last_name + obj.first_name, food[0]))

    @classmethod
    def drinking(cls, obj):
        drink = random.choice(drink_list) 
        obj.energy_level += random.randint(drink[1],drink[2])
        obj.knowledge_level += random.randint(drink[3],drink[4])

        print("{0} consumed a(n) {1}".format(obj.last_name + obj.first_name, drink[0]))