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
    data = """3,4,3,1,2"""
    days = 18
else:
    data = response.text
    days = 80

data = [int(x) for x in data.split(",")]


def simulate_fish(days, data):
    fishes = [0 for i in range(9)]
    for fish in data:
        fishes[fish] += 1

    for day in range(1, days + 1):

        new_fishes = fishes[1:] + [0]
        new_fishes[8] += fishes[0]
        new_fishes[6] += fishes[0]
        fishes = new_fishes

    return sum(fishes)


# print(data)
print(f"Part 1: {simulate_fish(80, data)}")
print(f"Part 2: {simulate_fish(256, data)}")
