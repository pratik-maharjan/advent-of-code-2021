lines = []
part1val = 0
with open("day2-input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
horizontal = 0
vertical = 0
for l in lines:
    if l.startswith("forward"):
        horizontal += int(l.split(' ')[1])
    elif l.startswith("down"):
        vertical += int(l.split(' ')[1])
    elif l.startswith("up"):
        vertical -= int(l.split(' ')[1])
part1val = vertical * horizontal
print(part1val)

part2val = 0
aim = 0
horizontal = 0
vertical = 0
for l in lines:
    if l.startswith("forward"):
        horizontal += int(l.split(' ')[1])
        vertical += int(l.split(' ')[1]) * aim
    elif l.startswith("down"):
        aim += int(l.split(' ')[1])
    elif l.startswith("up"):
        aim -= int(l.split(' ')[1])
part2val = vertical * horizontal
print(part2val)