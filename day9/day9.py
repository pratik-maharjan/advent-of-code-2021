# Part 1
# Get input

lines = []
part1val = 0
with open("day9-input.txt") as file:
    for line in file:
        line = line.strip()
        lis = []
        lis[:0] = line
        for i in range(len(lis)):
            lis[i] = int(lis[i])
        lines.append(lis)
values = []
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        if row == 0 and col == 0:
            if (lines[row][col] < lines[row+1][col]) and (lines[row][col] < lines[row][col+1]):
                values.append(lines[row][col])
        elif row == 0 and col == len(lines[row])-1:
            if (lines[row][col] < lines[row+1][col]) and (lines[row][col] < lines[row][col-1]):
                values.append(lines[row][col])
        elif row == len(lines)-1 and col == 0:
            if (lines[row][col] < lines[row-1][col]) and (lines[row][col] < lines[row][col+1]):
                values.append(lines[row][col])
        elif row == len(lines)-1 and col == len(lines[row])-1:
            if (lines[row][col] < lines[row-1][col]) and (lines[row][col] < lines[row][col-1]):
                values.append(lines[row][col])
        elif row == 0 and (col != 0 or col != len(lines[row])-1):
            if (lines[row][col] < lines[row+1][col]) and (lines[row][col] < lines[row][col-1]) and (lines[row][col] < lines[row][col+1]):
                values.append(lines[row][col])
        elif row == len(lines)-1 and (col != 0 or col != len(lines[row])-1):
            if (lines[row][col] < lines[row-1][col]) and (lines[row][col] < lines[row][col-1]) and (lines[row][col] < lines[row][col+1]):
                values.append(lines[row][col])
        elif col == 0 and (row != 0 or row != len(lines)-1):
            if (lines[row][col] < lines[row-1][col]) and (lines[row][col] < lines[row+1][col]) and (lines[row][col] < lines[row][col+1]):
                values.append(lines[row][col])
        elif col == len(lines[row])-1 and (row != 0 or row != len(lines)-1):
            if (lines[row][col] < lines[row-1][col]) and (lines[row][col] < lines[row+1][col]) and (lines[row][col] < lines[row][col-1]):
                values.append(lines[row][col])
        else:
            if (lines[row][col] < lines[row-1][col]) and (lines[row][col] < lines[row+1][col]) and (lines[row][col] < lines[row][col-1]) and (lines[row][col] < lines[row][col+1]):
                values.append(lines[row][col])
for v in values:
    part1val += (v+1)
print(part1val)