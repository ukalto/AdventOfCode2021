import os


def getInput():
    directory = os.path.dirname(os.getcwd()) + "/Inputs"
    path = os.path.join(directory, "Day11.txt")
    file1 = open(path, 'r')
    arr = [[int(x) for x in l.replace("\n", "")] for l in file1]
    return arr


def biggerThan(number, input):
    for x in input:
        for y in x:
            if number <= y:
                return True
    return False


def flash_handler(input):
    flash_spots = []
    while biggerThan(10, input):
        for ix, x in enumerate(input):
            for iy, y in enumerate(x):
                if y >= 10:
                    flash_spots.append([ix, iy])
                    input = increase_adjacent_positions(input, ix, iy)
                    input = reset_flash_spots(flash_spots, input)
    return [len(flash_spots), input]


def increase_adjacent_positions(input, x, y):
    # vertical
    for i in range(x - 1, x + 2):
        if 0 <= i < len(input) and i != x:
            input[i][y] += 1
    # horizontal
    for i in range(y - 1, y + 2):
        if 0 <= i < len(input[0]) and i != y:
            input[x][i] += 1
    # left down
    if len(input) > x + 1 and 0 <= y - 1:
        input[x + 1][y - 1] += 1
    # right down
    if len(input) > x + 1 and len(input[0]) > y + 1:
        input[x + 1][y + 1] += 1
    # left up
    if 0 <= x - 1 and 0 <= y - 1:
        input[x - 1][y - 1] += 1
    # right up
    if 0 <= x - 1 and len(input[0]) > y + 1:
        input[x - 1][y + 1] += 1
    return input


def reset_flash_spots(flash_spots, input):
    for i in flash_spots:
        input[i[0]][i[1]] = 0
    return input


def partOne(steps):
    input = getInput()
    countFlashes = 0
    for i in range(steps):
        input = [[z + 1 for z in a] for a in input]
        flashHandler = flash_handler(input)
        countFlashes += flashHandler[0]
        input = flashHandler[1]
    return countFlashes


def grid_printer(input):
    string = ""
    for x in input:
        for y in x:
            string += str(y)
        string += "\n"
    print(string)


def partTwo():
    input = getInput()
    runs = 1
    while True:
        input = [[z + 1 for z in a] for a in input]
        flashHandler = flash_handler(input)
        if flashHandler[0] == 100:
            return runs
        input = flashHandler[1]
        runs += 1


if __name__ == '__main__':
    print("Day 11")
    print(f"Part 1: {partOne(100)}")
    print(f"Part 2: {partTwo()}")
