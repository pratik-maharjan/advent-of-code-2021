# Get input
lines = []
with open("day10-input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

##################################################################################################################
# Part 1

stack = []
corrupted = []
for line in lines:
    for bracket in line:
        if bracket in ["(", "{", "[", "<"]:
            stack.append(bracket)
        else:
            top_char = stack.pop()
            if top_char == '(':
                if bracket != ')':
                    corrupted.append(line)
                    break
            if top_char == '{':
                if bracket != '}':
                    corrupted.append(line)
                    break
            if top_char == '[':
                if bracket != ']':
                    corrupted.append(line)
                    break
            if top_char == '<':
                if bracket != '>':
                    corrupted.append(line)
                    break
legal = []
illegal = []
for line in corrupted:
    for char in line:
        if char in ["(", "{", "[", "<"]:
            legal.append(char)
        else:
            top_char = legal.pop()
            if top_char == '(':
                if char != ')':
                    illegal.append(char)
                    break
            if top_char == '{':
                if char != '}':
                    illegal.append(char)
                    break
            if top_char == '[':
                if char != ']':
                    illegal.append(char)
                    break
            if top_char == '<':
                if char != '>':
                    illegal.append(char)
                    break
points = 0
for char in illegal:
    if char == ')':
        points += 3
    elif char == ']':
        points += 57
    elif char == '}':
        points += 1197
    elif char == '>':
        points += 25137
part1val = points
print("Part 1: {}").format(part1val)

##################################################################################################################
# Part 2

autocomplete = []
for line in lines:
    incomplete = []
    if line not in corrupted:
        for bracket in line:
            if bracket in ["(", "{", "[", "<"]:
                incomplete.append(bracket)
            else:
                incomplete.pop()
        score = 0
        incomplete.reverse()
        for char in incomplete:
            if char == '(':
                score *= 5
                score += 1
            elif char == '{':
                score *= 5
                score += 3
            elif char == '[':
                score *= 5
                score += 2
            elif char == '<':
                score *= 5
                score += 4
        autocomplete.append(score)
middleIndex = (len(autocomplete) - 1)/2
part2val = sorted(autocomplete)[middleIndex]
print("Part 2: {}").format(part2val)