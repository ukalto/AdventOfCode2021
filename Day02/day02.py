import os

directory = os.path.dirname(os.getcwd()) + "\Inputs"
path = os.path.join(directory, "Day2.txt")


def partOne(horizontal, depth):
    file1 = open(path, 'r')
    lines = file1.readlines()
    for i in lines:
        y = i.split()
        if y[0] == "forward":
            horizontal += int(y[1])
        elif y[0] == "down":
            depth += int(y[1])
        elif y[0] == "up":
            depth -= int(y[1])
    return horizontal * depth


def partTwo(horizontal, depth, aim):
    file1 = open(path, 'r')
    lines = file1.readlines()
    for i in lines:
        y = i.split()
        if y[0] == "forward":
            horizontal += int(y[1])
            depth += int(y[1]) * aim
        elif y[0] == "down":
            aim += int(y[1])
        elif y[0] == "up":
            aim -= int(y[1])
    return horizontal * depth


if __name__ == '__main__':
    print("Day 2")
    print(f"Part 1: {partOne(0, 0)}")
    print(f"Part 2: {partTwo(0, 0, 0)}")
