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
TEST = True
if TEST:
    data = """16,1,2,0,4,2,7,1,2,14"""
    days = 18
else:
    data = response.text
    days = 80

data = [int(x) for x in data.split(",")]

print(data)

med = np.median(data)
print(med, med in data)

moves1 = []
moves2 = []

for crab in data:
    fuel = abs(crab - med)
    moves1.append(fuel)
    moves2.append((fuel * (fuel + 1)) / 2)

print("Part 1:", sum(moves1))
print("Part 2:", sum(moves2))
