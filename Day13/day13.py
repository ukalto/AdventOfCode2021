import os
import sys


def getInput():
    directory = os.path.dirname(os.getcwd()) + "/Inputs"
    path = os.path.join(directory, "Day13.txt")
    file1 = open(path, 'r')
    dots, folds = [], []
    check = True
    for l in file1:
        if l == '\n':
            check = False
        if check:
            dots.append(l.replace("\n", "").split(","))
        else:
            folds.append(l.replace("\n", ""))
    folds = list(filter(None, folds))
    return [dots, folds]


def find_max(dots):
    maxx, maxy = 0, 0
    for i in dots:
        if int(i[0]) > maxx:
            maxx = int(i[0])
        if int(i[1]) > maxy:
            maxy = int(i[1])
    return maxx, maxy


def partOne():
    input = getInput()
    dots = input[0]
    folds = input[1]
    xy = find_max(dots)
    test = (xy[1] + 1) * [(xy[0] + 1) * ["."]]
    # field = [(xy[0] + 1)][(xy[1] + 1)]
    # field = [["."] * (xy[0] + 1)] * (xy[1] + 1)
    for i in dots:
        print(i)

        test[int(i[1])][int(i[0])] = "1"
    print(test[0])
    print_field(test)


def print_field(field):
    str = ""
    for i in field:
        for j in i:
            str += j
        str += "\n"
    print(str)


def partTwo():
    pass


if __name__ == '__main__':
    print("Day 13")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
