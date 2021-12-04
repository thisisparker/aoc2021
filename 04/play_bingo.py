with open('bingo.txt') as f:
    bingo_input = [l.strip() for l in f.readlines()]

draws = [int(i) for i in bingo_input.pop(0).split(',')]

boards = []
new_board = []

for l in bingo_input:
    if l:
        new_board.append([int(d) for d in l.split()])
    elif new_board:
        boards.append(new_board)
        new_board = []

print('board_count', len(boards))
removed = 0

def check_winner(board):
    for row in board:
        if not any(d != -1 for d in row):
            return True
    for i in range(len(board[0])):
        if not any(row[i] != -1 for row in board):
            return True

    return False

def sum_board(board):
    winning_sum = 0
    for row in board:
        for i in row:
            winning_sum += i if i != -1 else 0
    return winning_sum

first_winner = None
winning_draw = None
final_winner = None
final_draw = None

for d in draws:
    for b in [unwon for unwon in boards if not check_winner(unwon)]:
        for row in b:
            if d in row:
                row[row.index(d)] = -1

        if check_winner(b):
            if not first_winner:
                first_winner = b
                winning_draw = d
            removed += 1
        
        if removed == 100:
            last_winner = b
            final_draw = d

    if final_draw:
        break

winning_sum = sum_board(first_winner)
print('part 1 answer is', winning_draw * winning_sum)

final_winning_sum = sum_board(last_winner)
print('part 2 answer is', final_draw * final_winning_sum)
