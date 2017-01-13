import codecool_class
import random

laptop_list = [["Codewars", -5, 0, 0, 15],
               ["watch porn", 5, 10, -5, 0],
               ["use Google", -5, 0, 3, 7],
               ["do the project", -1, 0, 1, 6],
               ["watch a film", -2, 0, 2, 5],
               ["play Passsziánsz", -3, 0, 3, 4],
               ["order a guminő", -4, 0, 4, 7],
               ["use Windows Movie Maker", -5, 0, 5, 10],
               ["skype with Putyin", -6, 0, 6, 9],
               ["launch the apollo program", -5, 0, 6, 7],
               ["watch funny cats", -4, 0, 5, 8]]
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
            plus_k = random.randint(-10, 20)
            plus_e = random.randint(-10, 0)
            student.energy_level += plus_e
            student.knowledge_level += plus_k
            print("{} {} read a book, called \033[94m{}\033[0m".format(student.first_name,
                                                                       student.last_name, random.choice(
                                                                           book_list)))

    @classmethod
    def laptoping(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            laptop = random.choice(laptop_list)
            plus_k = random.randint(laptop[1], laptop[2])
            plus_e = random.randint(laptop[3], laptop[4])
            student.energy_level += plus_e
            student.knowledge_level += plus_k
            print("{} {} used the laptop for \033[94m{}\033[0m".format(student.last_name,
                                                                       student.first_name, laptop[0]))

    @classmethod
    def make_presentation(cls):
        for student in codecool_class.CodecoolClass.STUDENTS_LIST:
            plus_k = random.randint(2, 10)
            plus_e = random.randint(-8, 2)
            student.energy_level += plus_e
            student.knowledge_level += plus_k
        print("You done with the presentation")
