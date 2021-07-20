# -*- coding: euc-kr -*-
from graphics import *


def main():
    f = open("1.txt", "r")
    data = f.read()
    words = data.split(' ')
    wordList = list(set(words))
    win = GraphWin("Text", 100*len(wordList), 500)
    space = 0
    for word in wordList:
        r = Rectangle(Point(30+space, 450),
                      Point(80+space, 450-(words.count(word)*20)))
        r.setOutline(color_rgb(0, 0, 0))
        r.setFill(color_rgb(0, 0, 0))
        r.draw(win)
        message = Text(Point(55+space, 475), word)
        message.draw(win)
        space += 100
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
