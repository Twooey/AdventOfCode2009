import re


with open("day3.in", "r") as f:
    wires_points = [line.split(",") for line in f.read().splitlines()]

print(wires_points[0])

for element in wires_points[0]:
    match = re.match("(\w+)(\d+)", element)
print(match[0])


