import os


def getAsciiSum(word):
    sum = 0
    for letter in word:
        sum += ord(letter)
    return sum


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day8.txt")
    file1 = open(path, 'rt')
    arr = [[x for x in l.replace("\n", "").split(" | ")] for l in file1]
    return arr


def get2DArr(input):
    arr = []
    for i in input:
        arr.append(i.split(" "))
    return arr


def partOne():
    input = getInput()
    count = 0
    for i in input:
        two_d = get2DArr(i)
        for x in two_d[1]:
            if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
                count += 1
    return count


# def partTwo():
#     0-9
#     compareValues = [getAsciiSum("cagedb"), getAsciiSum("ab"), getAsciiSum("gcdfa"), getAsciiSum("fbcad"), getAsciiSum("eafb"),
#                      getAsciiSum("cdfbe"), getAsciiSum("cdfgeb"), getAsciiSum("dab"), getAsciiSum("acedgfb"), getAsciiSum("cefabd")]
#     input = getInput()
#     sum = 0
#     for i in input:
#         two_d = get2DArr(i)
#         for curr in two_d:
#             string = ""
#             for l in curr:
#                 asci = getAsciiSum(l)
#                 if compareValues.__contains__(asci):
#                     string += str(compareValues.index(asci))
#             print(string)
#     return sum


# pre condition is that all strings are having an equal length
def getDiff(str1, str2, str3):
    arr1 = list(str1)
    arr1.sort()
    arr2 = list(str2)
    arr2.sort()
    arr3 = list(str3)
    arr3.sort()
    diffs = []
    diffs.append(list(set(arr1) - set(arr2)))
    diffs.append(list(set(arr2) - set(arr3)))
    diffs.append(list(set(arr3) - set(arr1)))
    return diffs


def getPositions(arr):
    number = [""] * 8
    number[2:4] = getDiff(arr[6], arr[7], arr[8])
    diff5 = getDiff(arr[3], arr[4], arr[5])
    for i in diff5:
        if number.__contains__(i) and number[2] != i:
            if number[3] == i:
                save = number[2]
                number[2] = i
                number[3] = save
                diff5.remove(i)
            else:
                save = number[2]
                number[2] = i
                number[4] = save
                diff5.remove(i)
            break
    number[1] = diff5[0]
    number[5] = diff5[1]
    print(number)


def partTwo():
    input = getInput()
    sum = 0
    for inp in input:
        str = ""
        first = inp[0].split(" ")
        second = inp[1].split(" ")
        first = sorted(first, key=lambda x: (len(x), x))
        # print(first)
        getPositions(first)
        for number in second:
            if len(number) == 2:
                str += "1"
            elif len(number) == 4:
                str += "4"
            elif len(number) == 3:
                str += "7"
            elif len(number) == 7:
                str += "8"


if __name__ == '__main__':
    print("Day 8")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
