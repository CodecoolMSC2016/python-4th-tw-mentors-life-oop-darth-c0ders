import os

USER_STEPS = 0
MENU_ITEMS = ["MenuItem 1", "MenuItem 2", "MeunItem 3", "MenuItem 4"]
MENU_POSITION = 0


def getchar():
    # Returns a single character from standard input
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
        if MENU_POSITION > 0:
            MENU_POSITION = MENU_POSITION - 1
    elif direction == "down":
        if MENU_POSITION < len(MENU_ITEMS) - 1:
            MENU_POSITION = MENU_POSITION + 1

    for i in range(len(MENU_ITEMS)):
        if MENU_POSITION == i:
            cursor = " > "
        else:
            cursor = ""
        print(cursor + MENU_ITEMS[i])


def steps():
    global USER_STEPS
    global MENU_POSITION
    while USER_STEPS < 10:
        chr = getchar()
        if chr == "w":
            draw_menu("up")
        elif chr == "s":
            draw_menu("down")
        elif chr == "\r":
            USER_STEPS += 1
            print("STEP: " + str(MENU_POSITION))
            draw_menu("")
        elif chr == "q":
            exit()

steps()
