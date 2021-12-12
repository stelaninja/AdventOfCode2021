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
    data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

else:
    data = response.text


# data = [int(x) for y in data.strip().split("\n") for x in y]
data = [x for x in data.strip().split("\n")]

opens = "([{<"
closes = ")]}>"

valids = {"]": "[", ")": "(", "}": "{", ">": "<"}

point_table = {")": 3, "]": 57, "}": 1197, ">": 25137}

open_stack = []
failures = []

for line in data:
    for c in line:
        print(c)
        if c in opens:
            open_stack.append(c)
        elif c in closes:
            if valids[c] == open_stack[-1]:
                open_stack.pop()
            else:
                failures.append(c)
                break
        else:
            continue

# print(open_stack)
print("Failures:", failures)

points = 0

for fail in failures:
    points += point_table[fail]


print("Part 1:", points)
