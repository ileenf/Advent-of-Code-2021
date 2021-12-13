from collections import defaultdict

def check_win(board):
    for i in range(len(board)):
        if all(c == -1 for c in (board[i])):
            return True
    for j in range(len(board[0])):
        if all(board[i][j] == -1 for i in range(len(board))):
            return True
    return False

def get_score(board):
    total = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if int(board[row][col]) != -1:
                total += int(board[row][col])
    return total

def draw_board(board, numbers):
    positions = defaultdict(list)
    for row in range(len(board)):
        for col in range(len(board[row])):
            num = board[row][col]
            positions[num].append((row,col))

    for i in range(len(numbers)):
        num = numbers[i]
        position = positions[num]
        for pos in position:
            row = pos[0]
            col = pos[1]
            board[row][col] = -1

        if check_win(board):
            num_draws = i + 1
            score = get_score(board) * int(num)
            return num_draws, score



def giant_squid():
    file = open('/Users/ileenf/CS/aoc/aoc4.txt')

    i = 0
    numbers = ''
    board = []
    min_draws = 500
    curr_score = 0

    for line in file:
        line = line.strip()
        if i == 0:
            numbers = line
        else:
            if line.strip() == '':
                # calc
                if board:
                    num_draws, score = draw_board(board, numbers.split(','))
                    board = []

                    if num_draws < min_draws:
                        min_draws = num_draws
                        curr_score = score


            else:
                temp_board = []
                for num in line.split():
                    temp_board.append(num)
                board.append(temp_board)
        i+=1
    if board:
        num_draws, score = draw_board(board, numbers.split(','))
        board = []

    if num_draws < min_draws:
        min_draws = num_draws
        curr_score = score
    return curr_score


def giant_squid2():
    file = open('/Users/ileenf/CS/aoc/aoc4.txt')

    i = 0
    numbers = ''
    board = []
    min_draws = -1
    curr_score = 0

    for line in file:
        line = line.strip()
        if i == 0:
            numbers = line
        else:
            if line.strip() == '':
                # calc
                if board:
                    num_draws, score = draw_board(board, numbers.split(','))
                    board = []

                    if num_draws > min_draws:
                        min_draws = num_draws
                        curr_score = score


            else:
                temp_board = []
                for num in line.split():
                    temp_board.append(num)
                board.append(temp_board)
        i+=1
    if board:
        num_draws, score = draw_board(board, numbers.split(','))
        board = []

    if num_draws > min_draws:
        min_draws = num_draws
        curr_score = score
    return curr_score

print(giant_squid2())