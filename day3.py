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
data = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

data = data.strip().split("\n")
data = [l for l in data]


def bit_rates(arr):
    if Counter(arr).most_common()[0][0] == "1":
        return "1", "0"
    else:
        return "0", "1"


# Part 1

arr = []

for d in data:
    arr.append(list(d))

arr = np.array(arr)
trans_arr = arr.T.tolist()
# print(trans_arr)

gamma_rate = []
epsilon_rate = []

for r in trans_arr:
    g, e = bit_rates(r)
    gamma_rate.append(g)
    epsilon_rate.append(e)


print("Part 1:", int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2))

# Part 2

oxygen_rating = list(arr)


while len(oxygen_rating) != 1:
    new_oxygen_rating = []
    step = 0

    for j in range(len(arr)):
        for i in range(step, len(trans_arr)):
            print(i, arr[i])
            if arr[j][i] == gamma_rate[i]:
                new_oxygen_rating.append([oxygen_rating[j]])
            step += 1
    oxygen_rating = new_oxygen_rating[:]
    print(oxygen_rating)

print(oxygen_rating)

