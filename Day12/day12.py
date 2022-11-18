import os


def getInput():
    directory = os.path.dirname(os.getcwd()) + "/Inputs"
    path = os.path.join(directory, "Day12.txt")
    file1 = open(path, 'r')
    arr = [l.replace("\n","").split("-") for l in file1]
    return arr


def partOne():
    print(getInput())


def partTwo():
    pass


if __name__ == '__main__':
    print("Day 12")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
