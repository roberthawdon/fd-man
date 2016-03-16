#!/usr/local/bin/python

import os
import curses

ScreenH = 0
ScreenW = 0


myscreen = curses.initscr()

ScreenH, ScreenW = myscreen.getmaxyx()

myscreen.addstr(0, 0, "Menu will go here")
myscreen.addstr(2, 0, "Directory listing will start here")
myscreen.addstr(ScreenH - 1, 0, "Bottom pannel here")
myscreen.refresh()
myscreen.getch()

curses.endwin()

os.system("clear")
print "SHOW Version 0.0.0"

