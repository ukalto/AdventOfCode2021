import os
import re


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day4.txt")
    file1 = open(path, 'r')
    raw_data = file1.read()
    return raw_data.split("\n\n")


def transformInput(data):
    my_array = []
    my_array.append(data[0].split(","))
    for i in range(1, len(data)):
        delimiters = "\n", " "
        regexPattern = '|'.join(map(re.escape, delimiters))
        list = re.split(regexPattern, data[i])
        list = [x for x in list if x]
        my_array.append(list)
    return my_array


def checkRows(my_array, number):
    for board in my_array:
        counter = 0
        for i in range(len(board)):
            if i != 0 and i % 5 == 0:
                counter = 0
            if int(board[i]) == -1:
                counter += 1
            if counter == 5:
                return calcScore(board, number)
    return 0


def checkColumns(my_array, number):
    for board in my_array:
        z = 5
        x = 0
        y = 0
        counter = 0
        while (x + 1) * (y + 1) < len(board):
            if y != 0 and y % 5 == 0:
                x += 1
                y = 0
                counter = 0
            if int(board[(z * y) + x]) == -1:
                counter += 1
            if counter == 5:
                return calcScore(board, number)
            y += 1
    return 0


def calcScore(board, last_value):
    sum = 0
    for i in board:
        if i != -1:
            sum += int(i)
    return sum * int(last_value)


def partOne():
    my_array = transformInput(getInput())
    bingo_numbers = my_array.pop(0)
    for number in bingo_numbers:
        for board in my_array:
            for i in range(len(board)):
                if board[i] == number:
                    board[i] = -1
        if checkRows(my_array, number) != 0:
            return checkRows(my_array, number)
        elif checkColumns(my_array, number) != 0:
            return checkColumns(my_array, number)


def deleteRowWins(my_array):
    curr = my_array.copy()
    deleted = 0
    for idx, board in enumerate(my_array):
        counter = 0
        for i in range(len(board)):
            if len(curr) == 1: return curr
            if i != 0 and i % 5 == 0:
                counter = 0
            if int(board[i]) == -1:
                counter += 1
            if counter == 5:
                del curr[idx - deleted]
                deleted += 1
                break
    return curr


def deleteColumnWins(my_array):
    curr = my_array.copy()
    deleted = 0
    for idx, board in enumerate(my_array):
        z = 5
        x = 0
        y = 0
        counter = 0
        while (x + 1) * (y + 1) < len(board):
            if len(curr) == 1: return curr
            if y != 0 and y % 5 == 0:
                x += 1
                y = 0
                counter = 0
            if int(board[(z * y) + x]) == -1:
                counter += 1
            if counter == 5:
                del curr[idx - deleted]
                deleted += 1
                break
            y += 1
    return curr


def partTwo():
    my_array = transformInput(getInput())
    bingo_numbers = my_array.pop(0)
    for number in bingo_numbers:
        if len(my_array) == 1: return my_array
        for board in my_array:
            for i in range(len(board)):
                if board[i] == number:
                    board[i] = -1
        my_array = deleteColumnWins(deleteRowWins(my_array))
        if len(my_array) == 1:
            return calcScore(my_array[0], number)


if __name__ == '__main__':
    print("Day 4")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
