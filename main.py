import curses
import atexit

stdscr = curses.initscr()

def cleanup():
  #To terminate application
  curses.nocbreak(); stdscr.keypad(0); curses.echo()
  curses.endwin()

def update(num):
  print(num)

atexit.register(cleanup)

curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.use_default_colors()
curses.noecho()    #Stop keyboard input from being displayed
curses.cbreak()    #Stop requiring enter for keypresses to be handled

stdscr.keypad(1)   #Get keypad ready for input

dims = stdscr.getmaxyx()

lines = ["+------------+------------+------------+------------+------------+\n",
         "|            |            |            |            |            |\n",
         "|    Health  |    Food    |    Toilet  |    Games   |   Connect  |\n",
         "|            |            |            |            |            |\n",
         "+------------+------------+------------+------------+------------+\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                      Insert Tamagotchi Here                    |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "|                                                                |\n",
         "+------------+------------+------------+------------+------------+\n",
         "|            |            |            |            |            |\n",
         "| Discipline | Medication |   Lights   |  Notebook  |  Attention |\n",
         "|            |            |            |            |            |\n",
         "+------------+------------+------------+------------+------------+\n"]

iterlines = iter(lines)   #Iterate through lines list

for str in iterlines:
  stdscr.addstr(str)

stdscr.refresh()
selector = 0
input = 0
while input != 27:
  print(input)
  input = stdscr.getch()

  #arrow keys 258-down 259-up 260-left 261-right
  if input == 258:
    print()
    #down arrow does nothing here
  if input == 259:
    print()
    #up arrow does nothing here
  if input == 260:
    if selector == 1:
      selector = 10
      update(selector)
    elif selector != 0:
      selector = selector - 1
      update(selector)
  if input == 261:
    if selector == 10:
      selector = 1
      update(selector)
    else: 
      selector = selector + 1
      update(selector)
