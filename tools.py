import codecool_class
import random

laptop_list = [["do_codewars", -5, 0, 0, 15], ["watch_porn", 5, 10, -5, 0], ["use_google", -5, 0, 3, 8]]
book_list = ["Clean Code",
             "World of Mein Kampf",
             "Winnie the pooh and the 100 moons pagony",
             "Kama Sutra",
             "Tibi atya füves könyve",
             "History of Coca-Cola",
             "Lord of the drinks",
             "Harry Potter and the epe köve",
             "Szepesi Niki - I am the szexmániás",
             "Wish it Want it Do it",
             "Hangóver",
             "Szárazföldi emlősök II.",
             "Anyanyelvünk II. osztály",
             "2 girls one kap",
             "Ablakzsiráf",
             "Pál úcai lányok",
             "Toldi V. (A gépek támdása)",
             "Dzseki Csen: Szia",
             "Stohl András: Rácsok mögött"]


class Tools:

    @classmethod
    def read_book(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            student.energy_level += random.randint(-10, 0)
            student.knowledge_level += random.randint(0, 10)
            print("{} {} read a book, called \033[94m{}\033[0m | E: {} K: {}".format(student.first_name,
                                                                                     student.last_name, random.choice(
                                                                                         book_list),
                                                                                     student.energy_level,
                                                                                     student.knowledge_level))

    @classmethod
    def laptoping(cls, obj):
        laptop = random.choice(laptop_list)
        obj.energy_level += random.randint(laptop[1], laptop[2])
        obj.knowledge_level += random.randint(laptop[3], laptop[4])

        print("{0} consumed a(n) {1}".format(obj.last_name + obj.first_name, laptop[0]))

    @classmethod
    def make_presentation(cls, student):
        student.energy_level += random.randint(-12, -6)
        student.knowledge_level += random.randint(2, 8)
