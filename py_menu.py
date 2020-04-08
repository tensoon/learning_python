import curses


def main(stdscr):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
