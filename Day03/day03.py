import os

directory = os.path.dirname(os.getcwd()) + "\Inputs"
path = os.path.join(directory, "Day3.txt")


def calcGamma():
    file1 = open(path, 'r')
    raw_data = file1.read()
    lines = raw_data.split("\n")
    gamep = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in lines:
        counter = 0
        for character in line:
            saveVal = int(character)
            if saveVal != 1:
                saveVal = -1
            gamep[counter] += saveVal
            counter += 1
    output = ""
    for i in gamep:
        if int(i) <= 0:
            output += "0"
        else:
            output += "1"
    return output


def reverseBits(input):
    output = ""
    for i in input:
        if int(i) == 0:
            output += "1"
        else:
            output += "0"
    return output


def getCO2Oxygen(check):
    file1 = open(path, 'r')
    raw_data = file1.read()
    lines = raw_data.split("\n")
    pos = 0
    x = '1'
    if not check:
        x = '0'
    while len(lines) > 1:
        count_zero = 0
        count_one = 0
        curr_list = []
        for line in lines:
            if line[pos] == '0':
                count_zero += 1
            else:
                count_one += 1
        for line in lines:
            if count_one >= count_zero:
                if line[pos] == x:
                    curr_list.append(line)
            else:
                if line[pos] != x:
                    curr_list.append(line)
        lines = curr_list
        pos += 1
    return int(lines[0], 2)


if __name__ == '__main__':
    print("Day 3")
    print(f"Part 1: {int(reverseBits(calcGamma()), 2) * int(calcGamma(), 2)}")
    print(f"Part 2: {getCO2Oxygen(True) * getCO2Oxygen(False)}")
