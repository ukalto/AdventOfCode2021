import os


def getInput():
    directory = os.path.dirname(os.getcwd()) + "\Inputs"
    path = os.path.join(directory, "Day6.txt")
    file1 = open(path, 'r')
    raw_data = file1.read()
    return raw_data.split(",")


def fillArray(raw_data):
    arr = []
    for i in raw_data:
        arr.append(int(i))
    return arr


def partOne():
    arr = fillArray(getInput())
    for day in range(80):
        count_zeros = 0
        for index in range(len(arr)):
            if arr[index] == 0:
                arr[index] = 6
                count_zeros += 1
            else:
                arr[index] -= 1
        for i in range(count_zeros):
            arr.append(8)
    return len(arr)


def partTwo():
    # 0,1,2,3,4,5,6,7,8
    days = [0] * 9
    arr = fillArray(getInput())
    for index in arr:
        days[index] += 1
    for i in range(256):
        today = i % len(days)
        days[(today + 7) % len(days)] += days[today]
    return sum(days)


if __name__ == '__main__':
    print("Day 6")
    print(f"Part 1: {partOne()}")
    print(f"Part 2: {partTwo()}")
