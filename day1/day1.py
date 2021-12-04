lines = []
part1val = 0
with open("day1-input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(int(line))
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        part1val += 1
print part1val

part2val = 0
combination = []
for i in range(0, len(lines)-2):
    sum = lines[i] + lines[i+1] + lines[i+2]
    combination.append(sum)
for i in range(1, len(combination)):
    if combination[i] > combination[i-1]:
        part2val += 1
print part2val