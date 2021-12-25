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


# Extract the points and convert them to integers
points = [[int(y) for y in x.split(",")] for x in data[0].split("\n")]

# Extract the fold instructions
folds = [x.split()[-1].split("=") for x in data[1].strip().split("\n")]

# Create an array with the size based on the max point values
max_x = max([x[0] for x in points]) + 1
max_y = max([y[1] for y in points]) + 1
paper = np.zeros((max_y, max_x))

# Create points on the paper
for point in points:
    paper[point[1], point[0]] = 1


def fold_paper(exp, arr):
    """
    Function to fold the paper on the fold line.
    Returns the folded array.
    """

    # Get the folding instructions
    line = int(exp[1])

    if exp[0] == "x":
        p1 = arr[:, :line]
        p2 = arr[:, line + 1 :]
        # Flip the second half horizontally
        p2 = np.flip(p2, axis=1)
    else:
        p1 = arr[:line, :]
        p2 = arr[line + 1 :, :]
        # Flip the second half vertically
        p2 = np.flip(p2, axis=0)

    return p1 + p2


# Create the first fold and print the sum of points
first_fold = fold_paper(folds[0], paper)
print(f"Part 1: {(first_fold > 0).sum()}")

# Make all the folds
for fold in folds:
    paper = fold_paper(fold, paper)

# Print the paper
print("Part 2:")
for line in paper:
    for c in line:
        if c > 0:
            print("#", end="")
        else:
            print(" ", end="")
    print()
