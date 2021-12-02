import os
import re
import sys
import requests

SESSION_KEY = {"session": os.environ.get("SESSION_KEY", None)}
DAY = int(re.findall(r"[0-9]", sys.argv[0].split("/")[-1])[0])


response = requests.get(
    f"https://adventofcode.com/2021/day/{DAY}/input", cookies=SESSION_KEY
)

data = response.text

data = data.strip().split("\n")
data = list(map(int, data))

# Part 1
result = 0
high = data[0]
for num in data[1:]:
    if num > high:
        result += 1
    high = num

print("Part 1:", result)

# Part 2
n = 1
result = 0
high = sum(data[0:3])
# print(data[:30])
while n + 3 <= len(data):
    num = sum(data[n : n + 3])
    if num > high:
        result += 1

    # print(n, num, data[n: n +3])

    high = num
    n += 1

print("Part 2:", result)
