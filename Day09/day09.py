import os


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day9.txt")
    file1 = open(path, 'r')
    arr = [[x for x in l.replace("\n", "")] for l in file1]
    return arr


def partOne():
    input = getInput()
    numbers = []
    for y in range(len(input)):
        for x in range(len(input[y])):
            count = 0
            check = 0
            if x - 1 >= 0:
                check += 1
                if input[y][x] < input[y][x - 1]:
                    count += 1
            if x + 1 < len(input[y]):
                check += 1
                if input[y][x] < input[y][x + 1]:
                    count += 1
            if y - 1 >= 0:
                check += 1
                if input[y][x] < input[y - 1][x]:
                    count += 1
            if y + 1 < len(input):
                check += 1
                if input[y][x] < input[y + 1][x]:
                    count += 1
            if count == check:
                numbers.append(int(input[y][x]))
    return sum(numbers) + len(numbers)


def partTwo():
    pass


if __name__ == '__main__':
    print("Day 9")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
