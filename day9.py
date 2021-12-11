import os
import re
import sys
import requests
import numpy as np
from collections import Counter
from dotenv import load_dotenv
from scipy.signal import find_peaks

load_dotenv("./.env")

SESSION_KEY = {"session": os.environ.get("SESSION_KEY", None)}
DAY = int(re.findall(r"[0-9]", sys.argv[0].split("/")[-1])[0])

response = requests.get(
    f"https://adventofcode.com/2021/day/{DAY}/input", cookies=SESSION_KEY
)

# TEST DATA
TEST = False
if TEST:
    data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

else:
    data = response.text


# data = [int(x) for y in data.strip().split("\n") for x in y]
data = [x for x in data.strip().split("\n")]
arr_width = len(data[0])
arr_height = len(data)


data = [int(x) for y in data for x in y]
data = np.array(data)
data = np.reshape(data, (arr_height, arr_width))

a = np.pad(
    data, (1, 1), mode="constant", constant_values=(np.amax(data), np.amax(data))
)
loc_min = []
rows = a.shape[0]
cols = a.shape[1]

for ix in range(rows - 1):
    for iy in range(cols - 1):
        if (
            a[ix, iy] < a[ix, iy + 1]
            and a[ix, iy] < a[ix, iy - 1]
            and a[ix, iy] < a[ix + 1, iy]
            and a[ix, iy] < a[ix + 1, iy - 1]
            and a[ix, iy] < a[ix + 1, iy + 1]
            and a[ix, iy] < a[ix - 1, iy]
            and a[ix, iy] < a[ix - 1, iy - 1]
            and a[ix, iy] < a[ix - 1, iy + 1]
        ):
            temp_pos = (ix - 1, iy - 1)
            loc_min.append(temp_pos)


# low_point_matrix = lows

print(data)
print(len(data))
# print(low_point_matrix)
print(loc_min)

result = 0

for point in loc_min:
    result += data[point] + 1

print("Part 1:", result)
