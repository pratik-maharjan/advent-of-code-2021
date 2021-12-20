# Part 1

# Get input
lines = []
part1val = 0
with open("day5-input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

position = {}
for line in lines:
    points = line.replace(" -> ", ",").strip().split(",")
    points = list(map(int, points))
    x1, y1, x2, y2 = int(points[0]), int(points[1]), int(points[2]), int(points[3])
    if x1 == x2:
        # vertical 
        for x in range(min(y1, y2), max(y1, y2)+1):
            if position.has_key((x1, x)):
                value = position.get((x1, x))
            else:
                position[(x1, x)] = 0
                value = position.get((x1, x))
            position[(x1, x)] = value + 1
    elif y1 == y2:
        # horzontal 
        for x in range(min(x1, x2), max(x1, x2)+1):
            if position.has_key((x, y1)):
                value = position.get((x, y1))
            else:
                position[(x, y1)] = 0
                value = position.get((x, y1))
            position[(x, y1)] = value + 1

for val in position.values():
    if val > 1:
        part1val += 1
print("Part 1: {}").format(part1val)

##############################################################
# Part 2

part2val = 0
position = {}
for line in lines:
    points = line.replace(" -> ", ",").strip().split(",")
    points = list(map(int, points))
    x1, y1, x2, y2 = int(points[0]), int(points[1]), int(points[2]), int(points[3])
    if x1 == x2:
        # vertical 
        for x in range(min(y1, y2), max(y1, y2)+1):
            if position.has_key((x1, x)):
                value = position.get((x1, x))
            else:
                position[(x1, x)] = 0
                value = position.get((x1, x))
            position[(x1, x)] = value + 1
    elif y1 == y2:
        # horzontal 
        for x in range(min(x1, x2), max(x1, x2)+1):
            if position.has_key((x, y1)):
                value = position.get((x, y1))
            else:
                position[(x, y1)] = 0
                value = position.get((x, y1))
            position[(x, y1)] = value + 1
    else:
        # find the direction of the diagonal line
        if x1 < x2:
            x_d = 1
        else:
            x_d = -1
        
        if y1 < y2:
            y_d = 1
        else:
            y_d = -1
        
        x, y = x1, y1
        while (x, y) != (x2 + x_d, y2 + y_d):
            if position.has_key((x, y)):
                value = position.get((x, y))
            else:
                position[(x, y)] = 0
                value = position.get((x, y))
            position[(x, y)] = value + 1
            x, y = x + x_d, y + y_d

for val in position.values():
    if val > 1:
        part2val += 1
print("Part 2: {}").format(part2val)
