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
    res = Counter(arr).most_common()[0][0]
    if res == "1":
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


def get_most(arr):
    res = Counter(arr).most_common()
    print(res)
    if res[0][1] == res[1][1]:
        return "1"
    elif res[0][0] == "0":
        return "0"
    else:
        return "1"


ox_arr = arr[:]

oxygen_rating = ""

while len(ox_arr) > 1:
    trans_ox_arr = np.array(ox_arr).T.tolist()
    new_ox_arr = []
    for i, r in enumerate(ox_arr):
        if get_most(r) == r[i]:
            new_ox_arr.append(r)

    ox_arr = new_ox_arr[:]
    print("ox_arr", ox_arr)
    # oxygen_rating += get_most(r)

print(ox_arr)
print(oxygen_rating)

