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

# TESTED ANSWERS
# Part 2:
# 98231561 (too low) round move
# 98231570 (too low) round data
# 98231739 (too high) round sum

# TEST DATA
TEST = False
if TEST:
    data = """16,1,2,0,4,2,7,1,2,14"""
else:
    data = response.text

data = [int(x) for x in data.split(",")]

# print(data)

med = np.median(data)
mean = np.mean(data)
# print(med, med in data)
print(mean)

moves1 = []
moves2 = []

for crab in data:
    fuel1 = abs(crab - med)
    # fuel2 = abs(crab - mean)
    moves1.append(fuel1)
    # moves2.append(round((fuel2 * (fuel2 + 1)) / 2))

minimum = 1e9
position = None
print(minimum)

for i in range(int(mean) - 5, int(mean) + 5):
    moves2 = []
    for crab in data:
        fuel = abs(crab - i)
        moves2.append(round((fuel * (fuel + 1)) / 2))

    res = sum(moves2)
    # print(minimum, res)
    if res < minimum:
        position = i
        minimum = res

print(position)

print("Part 1:", sum(moves1))
print("Part 2:", minimum)
