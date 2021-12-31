import os
import re
import sys
import requests
import numpy as np
from collections import Counter
from dotenv import load_dotenv

load_dotenv("./.env")

SESSION_KEY = {"session": os.environ.get("SESSION_KEY", None)}
DAY = int(re.findall(r"[0-9]+", sys.argv[0].split("/")[-1])[0])

response = requests.get(
    f"https://adventofcode.com/2021/day/{DAY}/input", cookies=SESSION_KEY
)

# TEST DATA
TEST = True

if TEST:
    data = """1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581"""

else:
    data = response.text

data = [[int(j) for j in i.strip()] for i in data.strip().split("\n")]

# print(data)


def expand_map(map, times=5):
    new_map = []
    for t in range(times):
        for row in map:
            row.extend([i + 1 if i < 9 else 1 for i in row])
            new_map.append(row)
            print(row)
        map = new_map

    return new_map


exp1 = expand_map(data)
print(exp1)

print("".join([str(i) for i in exp1[0]]))
print("11637517422274862853338597396444961841755517295286")

data[0][0] = 0


class Solution(object):
    def minPathSum(self, grid):
        row = len(grid) - 1
        column = len(grid[0]) - 1
        i = row - 1
        j = column - 1
        while j >= 0:
            grid[row][j] += grid[row][j + 1]
            j -= 1
        while i >= 0:
            grid[i][column] += grid[i + 1][column]
            i -= 1
        j = column - 1
        i = row - 1
        while i >= 0:
            while j >= 0:
                grid[i][j] += min(grid[i][j + 1], grid[i + 1][j])
                j -= 1
            j = column - 1
            i -= 1
        return grid[0][0]


ob1 = Solution()
print(ob1.minPathSum(data))
