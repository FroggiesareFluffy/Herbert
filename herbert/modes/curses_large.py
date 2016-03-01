import curses
import os


class Sprite(object):
    def __init__(self, filename):
        self.front = []
        self.back = []
        self.left = []
        self.right = []
        with open(os.path.join("..", "data", filename)) as spfile:
            current = 0
            images = [self.front, self.back, self.left, self.right]
            for line in spfile.readlines():
                if line == "!>!>!>!>!>!>!>!>!>!>!>!>":
                    current += 1
                else:
                    images[current].append(line.rstrip())


def main(scr):
    scr.leaveok()
