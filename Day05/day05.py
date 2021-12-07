import os


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day5.txt")
    file1 = open(path, 'rt')
    arr = [[int(x) for x in l.replace(" -> ", " ").replace(",", " ").split()] for l in file1]
    return arr


def calcAll(bool):
    rowCol = {}
    all = {}
    arr = getInput()
    for x1, y1, x2, y2 in arr:
        if x1 == x2:
            if y1 > y2: y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                rowCol[(x1, y)] = rowCol.get((x1, y), 0) + 1
                all[(x1, y)] = all.get((x1, y), 0) + 1
        elif y1 == y2:
            if x1 > x2: x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                rowCol[(x, y1)] = rowCol.get((x, y1), 0) + 1
                all[(x, y1)] = all.get((x, y1), 0) + 1
        else:
            if x1 > x2: x1, x2, y1, y2 = x2, x1, y2, y1
            for x in range(x1, x2 + 1):
                if y2 > y1:
                    y = y1 + (x - x1)
                else:
                    y = y1 - (x - x1)
                all[(x, y)] = all.get((x, y), 0) + 1
    if bool:
        return sum(d > 1 for d in rowCol.values())
    else:
        return sum(d > 1 for d in all.values())


def partOne():
    return calcAll(True)


def partTwo():
    return calcAll(False)


if __name__ == '__main__':
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
