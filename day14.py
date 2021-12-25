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
TEST = False

if TEST:
    data = """6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5"""

else:
    data = response.text

data = data.split("\n\n")

poly_template, poly_rules = data
poly_rules = [x.split(" -> ") for x in poly_rules.strip().split("\n")]

print(poly_rules)
CHUNK = 2

rules_dict = dict(poly_rules)


def grow_polymer(poly_template, chunk_size, steps=1):
    for j in range(steps):
        polymer = poly_template[0]
        for i in range(len(poly_template) - chunk_size + 1):
            # print(poly_template[i: i + chunk_size])
            rule = poly_template[i : i + chunk_size]
            if rule in rules_dict:
                polymer += rules_dict[rule] + rule[1:]
        poly_template = polymer

    return polymer


p1 = grow_polymer(poly_template, CHUNK, 10)

count1 = Counter(p1)

print(f"Part 1: {max(count1.values()) - min(count1.values())}")


## NOT FAST ENOUGH
# p2 = grow_polymer(poly_template, CHUNK, 40)

# print(f"Part 2: {max(count2.values()) - min(count2.values())}")
