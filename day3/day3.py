# Get input
lines = []
part1val = 0
with open("day3-input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
master = list(lines)

# Part 1
gamma = ''
epsilon = ''
for i in range(0, len(lines[0])):
    one = 0
    zero = 0
    for l in lines:
        if int(l[i]) == 0:
            zero += 1
        else:
            one += 1
    if zero >= one:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
gamma_rate = int(gamma, 2)
epsilon_rate = int(epsilon, 2)
part1val = gamma_rate * epsilon_rate
print("Part 1: {}").format(part1val)

# Part 2
def get_oxygen_rate(lines):
    for i in range(0, len(lines[0])):
        one = 0
        zero = 0
        oxygen_count = 0
        remove_list = []
        if len(lines) == 1:
            break
        for l in lines:
            if int(l[i]) == 0:
                zero += 1
            else:
                one += 1
        if one >= zero:
            oxygen_count = 1
        else:
            oxygen_count = 0
        for j in range(0, len(lines)):
            if int(lines[j][i]) != oxygen_count:
                remove_list.append(j)
        for x in sorted(remove_list, reverse=True):
            del lines[x]
    oxygen = int(lines[0], 2)
    return oxygen

def get_carbon_rate(lines):
    for i in range(0, len(lines[0])):
        one = 0
        zero = 0
        carbon_count = 0
        remove_list = []
        if len(lines) == 1:
            break
        for l in lines:
            if int(l[i]) == 0:
                zero += 1
            else:
                one += 1
        if one >= zero:
            carbon_count = 0
        else:
            carbon_count = 1
        for j in range(0, len(lines)):
            if int(lines[j][i]) != carbon_count:
                remove_list.append(j)
        for x in sorted(remove_list, reverse=True):
            del lines[x]
    carbon = int(lines[0], 2)
    return carbon

oxygen_rate = get_oxygen_rate(lines)
lines = list(master)
carbon_rate = get_carbon_rate(lines)
part2val = oxygen_rate * carbon_rate
print("Part 2: {}").format(part2val)