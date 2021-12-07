import os


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day7.txt")
    file1 = open(path, 'r')
    arr = [int(x) for x in file1.read().split(",")]
    return arr


def partOne():
    arr = getInput()
    smallest = float('inf')
    for x in range(len(arr)):
        count = 0
        for i in arr:
            count += abs(x + 1 - i)
        if count < smallest:
            smallest = count
    return smallest


def partTwo():
    arr = getInput()
    smallest = float('inf')
    for x in range(len(arr)):
        count = 0
        for i in arr:
            n = abs(x + 1 - i)
            count += (n * (n + 1)) / 2
        if count < smallest:
            smallest = count
    return int(smallest)


if __name__ == '__main__':
    print("Day 7")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
