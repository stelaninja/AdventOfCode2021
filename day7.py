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

# TEST DATA
TEST = False
if TEST:
    data = """16,1,2,0,4,2,7,1,2,14"""
else:
    data = response.text

data = [int(x) for x in data.split(",")]

med = np.median(data)
mean = np.mean(data)

moves1 = []
moves2 = []

for crab in data:
    fuel1 = abs(crab - med)
    fuel2 = abs(crab - int(mean))
    moves1.append(fuel1)
    moves2.append(round((fuel2 * (fuel2 + 1)) / 2))

print("Part 1:", sum(moves1))
print("Part 2:", sum(moves2))
