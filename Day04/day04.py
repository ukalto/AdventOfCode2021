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


def checkRows(board):
    counter = 0
    for i in range(len(board)):
        if i != 0 and i % 5 == 0:
            counter = 0
        if int(board[i]) == -1:
            counter += 1
        if counter == 5:
            return True

    return False


def checkColumns(board):
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
            return True
        y += 1
    return False


def calcScore(board, last_value):
    sum = 0
    for i in board:
        if i != -1:
            sum += int(i)
    return sum * int(last_value)


def partOne():
    my_array = transformInput(getInput())
    bingo_numbers = my_array[0]
    my_array.remove(bingo_numbers)
    for number in bingo_numbers:
        for board in my_array:
            for i in range(len(board)):
                if board[i] == number:
                    board[i] = -1
        for board in my_array:
            if checkRows(board) or checkColumns(board):
                return calcScore(board, number)


def removeEntries(list, removes):
    for r in removes:
        list.remove(r)
    return list


def getRounds(entry, numbers):
    count = 0
    for number in numbers:
        for i in range(len(entry)):
            if entry[i] == number:
                entry[i] = -1
        if checkRows(entry) or checkColumns(entry):
            return count
        else:
            count += 1


def partTwo():
    my_array = transformInput(getInput())
    bingo_numbers = my_array[0]
    my_array.remove(bingo_numbers)
    count = []
    for i in my_array:
        count.append(getRounds(i, bingo_numbers))
    var = 0
    for i in count:
        if var < i:
            var = i
    print(my_array[30])
    print(getRounds(my_array[29], bingo_numbers))
    return var


# def partTwo():
#     my_array = transformInput(getInput())
#     bingo_numbers = my_array[0]
#     my_array.remove(bingo_numbers)
#     while len(my_array) > 1:
#         number = bingo_numbers[0]
#         list_of_removes = []
#         for board in my_array:
#             for i in range(len(board)):
#                 if board[i] == number:
#                     board[i] = -1
#         for board in my_array:
#             if checkRows(board) or checkColumns(board):
#                 list_of_removes.append(board)
#         if len(list_of_removes) == len(my_array):
#             return getLastWhen(my_array[0], bingo_numbers)
#         else:
#             my_array = removeEntries(my_array, list_of_removes)
#         bingo_numbers.remove(number)
#     return getLastWhen(my_array[0], bingo_numbers)


# def getAllScores():
#     my_array = transformInput(getInput())
#     bingo_numbers = my_array[0]
#     my_array.remove(bingo_numbers)
#     x = 0
#     for i in my_array:
#         if x == 30:
#             return i
#         print(getLastWhen(i, bingo_numbers))
#         x += 1


if __name__ == '__main__':
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
    # 12635
    # ['35', '9', '82', '95', '40', '30', '10', '99', '7', '47', '12', '77', '54', '25', '34', '73', '97', '38', '11', '17', '70', '41', '87', '29', '57']
