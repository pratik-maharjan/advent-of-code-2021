# Part 1

# Get input
lines = []
part1val = 0
with open("day6-input.txt") as file:
    for line in file:
        lines = [int(x) for x in line.strip().split(",")]

days = 80
for i in range(0, days):
    for l in range(0, len(lines)):
        if lines[l] == 0:
            lines[l] = 6
            lines.append(8)
        else:
            lines[l] -= 1
part1val = len(lines)
print("Part 1: {}").format(part1val)

###############################################################
# Part 2
# This can be used for part one as well

# Get input
lines = []
part2val = 0
with open("day6-input.txt") as file:
    for line in file:
        lines = [int(x) for x in line.strip().split(",")]

days = 256
numbers = {}
for l in lines:
    if numbers.has_key(l):
        numbers[l] += 1
    else:
        numbers[l] = 1

for i in range(0, days):
    if numbers.has_key(0):
        new_numbers = {6: numbers[0], 8: numbers[0]}
    else:
        new_numbers = {6: 0, 8: 0}
    for key, value in numbers.items():
        if key > 0:
            if new_numbers.has_key(key-1):
                new_numbers[key-1] += value
            else:
                new_numbers[key-1] = 0
                new_numbers[key-1] += value
    numbers = new_numbers
part2val = sum(numbers.values())
print("Part 2: {}").format(part2val)