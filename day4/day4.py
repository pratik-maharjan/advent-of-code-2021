## Part 1
# Get input
part1val = 0
with open("day4-input.txt") as file:
    draw_numbers = [int(x) for x in file.readline().strip('\n').split(',')]
    cards = []
    while file.readline():
        card = []
        for i in range(5):
            card.extend([int(x) for x in file.readline().strip('\n').split(' ') if x != ''])
        cards.append(card)

# Set board
boards = []
for card in cards:
    board = []
    for c in card:
        board.append(False)
    boards.append(board)

# Find if a board has a winner
def find_winner(board):
    start = 0
    for i in range(5):
        if board[start] == True and board[start+1] == True and board[start+2] == True and board[start+3] == True and board[start+4] == True:
            return True
        start += 5
    start = 0
    for i in range(5):
        if board[start] == True and board[start+5] == True and board[start+10] == True and board[start+15] == True and board[start+20] == True:
            return True
        start += 1
    return False

# Get the total of sum from the winning board
def get_total(card, board):
    for i in range(len(board)):
        if board[i] == True:
            card[i] = 0
    val = 0
    for i in card:
        val += i
    return val

# Iterate to draw numbers and find the winner
found = False
while found is False:
    number = draw_numbers[0]
    draw_numbers = draw_numbers[1:]
    for a in range(len(cards)):
        for i in range(len(cards[a])):
            if  cards[a][i] == number:
                boards[a][i] = True
    for b in range(len(boards)):
        if find_winner(boards[b]):
            total = get_total(cards[b], boards[b])
            part1val = total * number
            found = True
print("Part 1: {}").format(part1val)

######################################################
## Part 2
# Get input
part2val = 0
with open("day4-input.txt") as file:
    draw_numbers = [int(x) for x in file.readline().strip('\n').split(',')]
    cards = []
    while file.readline():
        card = []
        for i in range(5):
            card.extend([int(x) for x in file.readline().strip('\n').split(' ') if x != ''])
        cards.append(card)

# Reset board
boards = []
for card in cards:
    board = []
    for c in card:
        board.append(False)
    boards.append(board)

# Iterate to draw numbers and find the winner and remove winning boards until the last one
found = False
while found is False:
    number = draw_numbers[0]
    draw_numbers = draw_numbers[1:]
    for a in range(len(cards)):
        for i in range(len(cards[a])):
            if  cards[a][i] == number:
                boards[a][i] = True
    index = 0
    while index < len(boards):
        if find_winner(boards[index]):
            if len(boards) > 1:
                boards.pop(index)
                cards.pop(index)

            else:
                found = True
                break
        else:
            index += 1

total = get_total(cards[0], boards[0])
part2val = total * number
print("Part 2: {}").format(part2val)
