import os
import statistics


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day10.txt")
    file1 = open(path, 'r')
    arr = [[x for x in l.replace("\n", "")] for l in file1]
    return arr


def partOne():
    input = getInput()
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    score_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    err_total = 0
    for x in input:
        count = []
        for y in x:
            if y in opening:
                count.append(y)
            elif y in closing and y == closing[opening.index(count[-1])]:
                count.pop()
            else:
                err_total += score_values[y]
                break
    return err_total


def partTwo():
    input = getInput()
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    score_values = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for x in input:
        count = []
        check = True
        score = 0
        for y in x:
            if y in opening:
                count.append(y)
            elif y in closing and y == closing[opening.index(count[-1])]:
                count.pop()
            else:
                check = False
                break
        if len(count) and check:
            for z in count[::-1]:
                score = score * 5 + score_values[z]
            scores.append(score)
    return statistics.median(scores)


if __name__ == '__main__':
    print("Day 10")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
