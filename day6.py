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
    for day in range(1, days + 1):
        new_fish = 0
        for i, fish in enumerate(data):
            if fish == 0:
                data[i] = 6
                new_fish += 1
            else:
                data[i] -= 1
        if new_fish > 0:
            data.extend([8] * new_fish)
        # print(f"{day} days: {data}")
    return len(data)


# print(data)
print(f"Part 1: {simulate_fish(80, data)}")
print(f"Part 2: {simulate_fish(256, data)}")
