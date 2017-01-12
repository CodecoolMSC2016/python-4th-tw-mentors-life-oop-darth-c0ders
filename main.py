import os
from codecool_class import *
from story import *
from kitchen import *
from lounge import *
from tools import *

USER_STEPS = 0
MENU_POSITION = 1
MENU_ITEMS = ["### MENU ###",
              "Check overall energy level",
              "Check overall knowledge level",
              "### ACTIONS ###",
              "Send them eat something",
              "Send them drink something",
              "Let them play PS",
              "Ask them for a darts battle",
              "Make them lay on beanbags",
              "Make them do dzsimnasztiksz",
              "Ask them to use laptops",
              "Make a presentation for them",
              "Read a book motherf*ckers",
              "This option makes absolutely nothing."]


def getchar():
    import tty
    import termios
    import sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def draw_steps():
    global USER_STEPS
    print("STEPS: " + str(USER_STEPS) + "/10 ", end="")
    print("| MENTOR: tesztMentor", end="")  # getMentorNaickname
    print("| CLASS: tesztClass", end="")  # getClassName
    print("\n" * 5)


def draw_menu(direction):
    global MENU_ITEMS
    global MENU_POSITION
    global USER_STEPS

    os.system("clear")
    draw_steps()

    if direction == "up":
        if MENU_POSITION > 1:
            MENU_POSITION = MENU_POSITION - 1
            if MENU_ITEMS[MENU_POSITION][0] == "#":
                MENU_POSITION = MENU_POSITION - 1
    elif direction == "down":
        if MENU_POSITION < len(MENU_ITEMS) - 1:
            MENU_POSITION = MENU_POSITION + 1
            if MENU_ITEMS[MENU_POSITION][0] == "#":
                MENU_POSITION = MENU_POSITION + 1

    for i in range(len(MENU_ITEMS)):
        if MENU_POSITION == i:
            cursor1, cursor2 = " > ", " < "
        else:
            cursor1, cursor2 = "| ", ""
        print(cursor1,
              MENU_ITEMS[i],
              cursor2)


def steps():
    global USER_STEPS
    global MENU_POSITION
    draw_menu("")
    while USER_STEPS < 10:
        chr = getchar()
        if chr == "w":
            draw_menu("up")
        elif chr == "s":
            draw_menu("down")
        elif chr == "\r":
            if MENU_POSITION > 3:
                USER_STEPS += 1
            print("STEP: " + str(MENU_POSITION))
            print(MENU_POSITION)
            draw_menu("")
            do_action()

        elif chr == "q":
            exit()
    Company.apply_for_company()


def wait_for_next():
    print("\nPress ENTER to continue")
    while getchar() != "\r":
        continue
    steps()


def do_action():
    os.system("clear")
    if MENU_POSITION == 1:
        CodecoolClass.check_class_energy()
    elif MENU_POSITION == 2:
        CodecoolClass.check_class_knowledge()
    elif MENU_POSITION == 4:
        Kitchen.eating()
    elif MENU_POSITION == 5:
        Kitchen.drinking()
    elif MENU_POSITION == 6:
        Lounge.playstationing()
    elif MENU_POSITION == 7:
        Lounge.dartsing()
    elif MENU_POSITION == 8:
        Lounge.beanbag()
    elif MENU_POSITION == 9:
        Lounge.gyming()
    elif MENU_POSITION == 10:
        Tools.laptoping()
    elif MENU_POSITION == 11:
        Tools.make_presentation()
    elif MENU_POSITION == 12:
        Tools.read_book()
    elif MENU_POSITION == 13:
        print("ASDASDASD")
    else:
        pass
    wait_for_next()

buildProgram()
steps()
