# Part 1
# Get input

lines = []
output = []
with open("day8-input.txt") as file:
    for line in file:
        line = line.strip().split(' | ')
        lines.append(line)
        output.append(line[1])

part1val = 0
for out in output:
    numbers = out.strip().split(' ')
    for num in numbers:
        if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:   # equals to 1 or 4 or 7 or 9 respectively
            part1val += 1
        else:
            continue
print("Part 1: {}").format(part1val)


############################################################################################
# Part 2

def decoder(pattern):
    numbers = pattern.strip().split(' ')
    for num in numbers:
        sorting = sorted(num)
        num = "".join(sorting)
    num_to_s = {}
    num_to_s[1], = 
    postions = ['x'] * 7
    for num in numbers:
        if len(num) == 7:
            postions[0] = num[3]
            postions[1] = num[0]
            postions[2] = num[5]
            postions[3] = num[6]
            postions[4] = num[1]
            postions[5] = num[4]
            postions[6] = num[2]
            print(num, postions)
        elif len(num) == 4:
            postions[6] = num[0]
            postions[1] = num[1]
            postions[2] = num[2]
            postions[3] = num[3]       
            print(num, postions)
        elif len(num) == 3:
            postions[0] = num[0]
            postions[1] = num[1]
            postions[3] = num[2]   
            print(num, postions)
        elif len(num) == 2:
            postions[1] = num[0]
            postions[3] = num[1]
            print(num, postions)
    return postions

def common(a, b):
    count = str()
    for char in a:
        if char in b:
            count += char
    return count

part2val = 0
for line in lines:
    pattern = line[0]
    output = line[1]
    output_numbers = output.strip().split(' ')
    for num in output_numbers:
        sorting = sorted(num)
        num = "".join(sorting)
    pattern_numbers = pattern.strip().split(' ')
    for num in pattern_numbers:
        sorting = sorted(num)
        num = "".join(sorting) 
    value = ''





    
    for num in numbers:
        if len(num) == 2:
            value = value + '1'
        elif len(num) == 4:
            value = value + '4'
        elif len(num) == 3:
            value = value + '7'
        elif len(num) == 7:
            value = value + '8'
        elif len(num) == 6:
            
        else:
            temp_positions = decoder(pattern)
            print(temp_positions)
            if temp_positions[5] not in num and temp_positions[6] not in num:
                value = value + '3'
            elif temp_positions[3] not in num and temp_positions[6] not in num:
                value = value + '2'
            elif temp_positions[1] not in num and temp_positions[5] not in num:
                value = value + '5'
            elif temp_positions[5] not in num:
                value = value + '9'
            elif temp_positions[1] not in num:
                value = value + '6'
            else:
                value = value + '0'
    print(value)
    part2val = part2val + int(value)
print("Part 2: {}").format(part2val)
