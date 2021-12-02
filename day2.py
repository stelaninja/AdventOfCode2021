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
data = [l.split() for l in data]

# Part 1
x = 0
y = 0

for command in data:
    move = int(command[1])
    if command[0] == "forward":
        x += move
    elif command[0] == "up":
        y -= move
    else:
        y += move


print("Part 1:", x * y)

# Part 2
x = 0
y = 0
aim = 0

for command in data:
    move = int(command[1])
    if command[0] == "forward":
        x += move
        y += move * aim

    elif command[0] == "up":
        aim -= move
    else:
        aim += move

print("Part 2:", x * y)
