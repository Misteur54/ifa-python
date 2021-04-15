import curses
import time


def main(stdscr):
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
        entry = stdscr.getch()
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(0, 0, f"{str(h)}, {str(w)}")
        if entry == curses.KEY_UP:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(10, 10, "je suis sur la touche du haut")
            stdscr.attroff(curses.color_pair(1))
            stdscr.refresh()
        if entry == curses.KEY_DOWN:
            stdscr.addstr(10, 10, "je suis sur la touche du bas")
            stdscr.refresh()
        if entry == curses.KEY_LEFT:
            stdscr.addstr(10, 10, "je suis sur la touche de gauche")
            stdscr.refresh()
        if entry == curses.KEY_RIGHT:
            stdscr.addstr(10, 10, "je suis sur la touche de droite")
            stdscr.refresh()

    curses.endwin()

if __name__ == "__main__":

    curses.wrapper(main)