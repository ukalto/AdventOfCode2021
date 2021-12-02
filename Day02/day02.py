import os

directory = os.path.dirname(os.getcwd()) + "\Inputs"
path = os.path.join(directory, "Day2.txt")


def calcPath1(horizontal, depth):
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


def calcPath2(horizontal, depth, aim):
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
    print("*Task 1*")
    print("Part 1")
    print(calcPath1(0, 0))
    print("Part 2")
    print(calcPath2(0, 0, 0))
