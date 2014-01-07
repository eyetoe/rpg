#!/usr/local/bin/python

from os import system
import curses

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Creating Character")
    screen.addstr(4, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with error"
    raw_input("Press enter")
    print ""

x = 0

while x != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Welcome To Outland")
    screen.addstr(3, 2, "  - Character Selection:")
    screen.addstr(4, 4, "   1 - Create")
    screen.addstr(5, 4, "   2 - Load")
    screen.addstr(6, 4, "   3 - Save")
    screen.addstr(7, 4, "   4 - Exit")
    screen.refresh()

    x = screen.getch()

    if x == ord('1'):
        char_race       = get_param("Choose Race; Dwarf-str, Elf-int, Human-con, Gnome-dex:")
        char_class      = get_param("Choose Class; Paladin, Sorcerer, Burgler, Druid:")
        char_alingment  = get_param("Choose Alingment; good, evil, neutral:")
        char_name       = get_param("Character Name:")
        curses.endwin()
        #execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
        print "Your character is: ", char_name, char_class, char_race, char_alingment
    if x == ord('2'):
        curses.endwin()
        #execute_cmd("df")
        #print "Loading Character..."
    #if x == ord('s'):
    if x == '3':
        curses.endwin()
        #execute_cmd("df -h")
        #print "Saving Character..."
    #if x == ord('x'):
    if x == '4':
        curses.endwin()
        #execute_cmd("df -h")
        #print "Exiting..."

curses.endwin()

