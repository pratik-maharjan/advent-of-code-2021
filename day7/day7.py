# Part 1 and 2

# Get input
lines = []
with open("day7-input.txt") as file:
    for line in file:
        lines = [int(x) for x in line.strip().split(",")]

part1val = float('inf')
part2val = float('inf')
for i in range(min(lines), max(lines)+1):
    total = 0
    temp = 0
    total_part_2 = 0
    for l in lines:
        diff = abs(l - i)
        temp = (diff*(diff+1))/2
        total += diff
        total_part_2 += temp
    part1val = min(total, part1val)
    part2val = min(total_part_2, part2val)
print("Part 1: {}").format(part1val)
print("Part 2: {}").format(part2val)