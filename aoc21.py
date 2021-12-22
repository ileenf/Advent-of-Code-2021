def check_win(player1_score, player2_score):
    # return number of losing player, 0 if no winner
    if player1_score >= 1000:
        return 2
    elif player2_score >= 1000:
        return 1

    return 0


def player_move(dice_roll, player_position):
    player_roll = 0

    for _ in range(3):
        player_roll += dice_roll
        dice_roll += 1
        if dice_roll == 101:
            dice_roll = 1

    curr_position = (player_position + player_roll) % 10
    if curr_position == 0:
        position = 10
    else:
        position = curr_position
    return position, dice_roll


def deterministic():
    file = open('/Users/ileenf/CS/aoc/tester.txt')

    lines = file.readlines()
    player1_position = int(lines[0].strip().split(':')[1])
    player2_position = int(lines[1].strip().split(':')[1])

    player1_score = 0
    player2_score = 0

    dice_roll = 1
    num_rolls = 0

    while True:
        # player 1 move
        player1_position, dice_roll = player_move(dice_roll, player1_position)
        num_rolls += 3
        player1_score += player1_position

        # check for winner
        status = check_win(player1_score, player2_score)
        if status == 1:
            return player1_score * num_rolls
        elif status == 2:
            return player2_score * num_rolls

        # player 2 move
        player2_position, dice_roll = player_move(dice_roll, player2_position)
        num_rolls += 3
        player2_score += player2_position

        # check for winner
        status = check_win(player1_score, player2_score)
        if status == 1:
            return player1_score * num_rolls
        elif status == 2:
            return player2_score * num_rolls


def generate_sums():
    res = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                res.append(a + b + c)
    return res


sums = generate_sums()
dp = {}

def split(player1_score, player1_position, player2_score, player2_position, player1_turn):
    if player1_score >= 21:
        return [1, 0]
    elif player2_score >= 21:
        return [0, 1]

    status = (player1_score, player1_position, player2_score, player2_position, player1_turn)
    if status in dp:
        return dp[status]

    p1_wins = 0
    p2_wins = 0
    for roll_sum in sums:
        if player1_turn:
            new_position = (player1_position + roll_sum) % 10
            if new_position == 0:
                new_score = 10
            else:
                new_score = new_position
            win1, win2 = split(player1_score + new_score, new_position, player2_score, player2_position, False)

        else:
            new_position = (player2_position + roll_sum) % 10
            if new_position == 0:
                new_score = 10
            else:
                new_score = new_position
            win1, win2 = split(player1_score, player1_position, player2_score + new_score, new_position, True)

        p1_wins += win1
        p2_wins += win2

    # store the result, i.e. THIS game state --> [p1_wins, p2_wins]
    dp[(player1_score, player1_position, player2_score, player2_position, player1_turn)] = [p1_wins, p2_wins]
    return [p1_wins, p2_wins]

def dirac():
    file = open('/Users/ileenf/CS/aoc/aoc21.txt')

    lines = file.readlines()
    player1_position = int(lines[0].strip().split(':')[1])
    player2_position = int(lines[1].strip().split(':')[1])

    print(max(split(0, player1_position, 0, player2_position, True)))


dirac()
