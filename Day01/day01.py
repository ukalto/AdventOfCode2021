import os

directory = os.path.dirname(os.getcwd()) +"\Inputs"
path = os.path.join(directory, "Day1.txt")


def countIncreas1():
    file1 = open(path, 'r')
    lines = file1.readlines()
    current = open(path).readline().rstrip()
    countI = 0
    for i in range(0, len(lines)):
        if lines[i] >= current:
            countI += 1
        current = lines[i]
    return countI


def countIncreas2():
    file1 = open(path, 'r')
    lines = file1.readlines()
    countI = 0
    old = 0
    for i in range(0, len(lines) - 2):
        current = 0
        for j in range(0, 3):
            if len(lines) > i + j:
                index = i + j
                current += int(lines[index])
        if old < current:
            countI += 1
        old = current
    return countI - 1


if __name__ == '__main__':
    print("*Task 1*")
    print("Part 1")
    print(countIncreas1())
    print("Part 2")
    print(countIncreas2())
