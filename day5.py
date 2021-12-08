import os
import re
import sys
import requests
import numpy as np
from collections import Counter
from dotenv import load_dotenv

load_dotenv("./.env")

SESSION_KEY = {"session": os.environ.get("SESSION_KEY", None)}
DAY = int(re.findall(r"[0-9]", sys.argv[0].split("/")[-1])[0])

response = requests.get(
    f"https://adventofcode.com/2021/day/{DAY}/input", cookies=SESSION_KEY
)

# data = response.text

# TESTED ANSWERS
# Part 1:
# 9070 wrong (too high)
# Part 2:
#

# TEST DATA
data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

# points = [x.split(" -> ") for y in data.split("\n") for x in y]
# points = [row for row in data.split("\n")]
points = [row.split(" -> ") for row in data.split("\n")]

x_list = []
y_list = []

for point in points:
    # x_list.extend(int(point.split(",")[:][0]))
    # print(point)
    x_list.extend([int(x) for x in re.findall(r"([0-9]+),", " ".join(point))])
    y_list.extend([int(y) for y in re.findall(r",([0-9]+)", " ".join(point))])
    # print(re.findall(r"([0-9]+),", " ".join(point)))
# x_list.extend([int(point[0].split(",")[0])])
# y_list.extend([int(point[0].split(",")[1])])

point_list = list(zip(x_list, y_list))

# print(max(x_list), x_list)

# print(max(y_list), y_list)

matrix = np.zeros((max(x_list) + 1, max(y_list) + 1))
# print(list(point_list))

while point_list:
    start, end = point_list[:2]
    point_list = point_list[2:]

    # if start[0] == end[0] or start[1] == end[1]:
    if (
        abs(start[0] - end[0]) == abs(start[1] - end[1])
        or start[0] == end[0]
        or start[1] == end[1]
    ):
        print(abs(start[0] - end[0]), start[0], end[0])
        if start[0] <= end[0]:
            xs = np.arange(start[0], end[0] + 1)
        else:
            xs = np.arange(end[0], start[0] + 1)
        if start[1] <= end[1]:
            ys = np.arange(start[1], end[1] + 1)
        else:
            ys = np.arange(end[1], start[1] + 1)
        # print(xs, ys)

        for x in xs:
            for y in ys:
                p = (x, y)
                # print("P:", p)
                matrix[p] += 1

        # print(start, end)

result = sum(sum(matrix > 1))

print(matrix)
print(f"Part 1: {result}")
