if __name__ == '__main__':
    from herbert.modes.text import main
    main()
    # import sys
    # try:
    #     import curses
    # except ImportError:
    #     from herbert.modes.text import main
    #     main()
    #     sys.exit()
    # try:
    #     stdscr = curses.initscr()
    # except curses.error:
    #     from herbert.modes.text import main
    #     main()
    #     sys.exit()
    # height, width = stdscr.getmaxyx()
    # if height > 5 and width > 20:
    #     from herbert.modes.curses_large import main
    #     curses.wrapper(main)
    # else:
    #     from herbert.modes.curses_small import main
    #     curses.wrapper(main)
