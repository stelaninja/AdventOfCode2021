import os
import re
import sys
import requests
import numpy as np
from collections import Counter

SESSION_KEY = {"session": os.environ.get("SESSION_KEY", None)}
DAY = int(re.findall(r"[0-9]", sys.argv[0].split("/")[-1])[0])


response = requests.get(
    f"https://adventofcode.com/2021/day/{DAY}/input", cookies=SESSION_KEY
)

# data = response.text

# TEST_DATA
data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

data = data.strip().split("\n")
data = [l for l in data]

numbers = list(map(int, data[0].split(",")))

boards = [list(map(int, b.strip().split())) for b in data[2:] if b]
# print(data[2:])

print(numbers)
print(boards)

board_arr = np.array(boards)
board_arr = np.reshape(board_arr, (3, 5, 5))
print(board_arr)

