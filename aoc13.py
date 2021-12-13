def origami():
    file = open('/Users/ileenf/CS/aoc/aoc13.txt')
    fold = []
    points = []
    folds = False
    for line in file:
        if folds:
            line = line.split()
            line = line[2].split('=')
            fold = [line[0], int(line[1])]
            break
        if line.strip() == '':
            folds = True

        else:
            line = line.strip().split(',')
            point = [int(line[0]), int(line[1])]
            points.append(point)

    direc = fold[0]
    location = int(fold[1])

    folded_points = set()
    if direc == 'x':
        for x, y in points:
            if x > location:
                temp_x = x - location
                new_x = location - temp_x
                folded_points.add((new_x, y))
            else:
                folded_points.add((x,y))
    elif direc == 'y':
        for x, y in points:
            if y > location:
                temp_y = y - location
                new_y = location - temp_y
                folded_points.add((x, new_y))
            else:
                folded_points.add((x,y))
    return len(folded_points)


def origami2():
    file = open('/Users/ileenf/CS/aoc/aoc13.txt')
    folds = []
    points = []
    on_folds = False
    for line in file:
        if on_folds:
            line2 = line.split()
            line2 = line2[2].split('=')
            fold = [line2[0], int(line2[1])]
            folds.append(fold)
            continue
        if line.strip() == '':
            on_folds = True

        else:
            line = line.strip().split(',')
            point = [int(line[0]), int(line[1])]
            points.append(point)

    for fold in folds:
        direc = fold[0]
        location = int(fold[1])

        folded_points = set()
        if direc == 'x':
            for x, y in points:
                if x > location:
                    temp_x = x - location
                    new_x = location - temp_x
                    folded_points.add((new_x, y))
                else:
                    folded_points.add((x,y))
        elif direc == 'y':
            for x, y in points:
                if y > location:
                    temp_y = y - location
                    new_y = location - temp_y
                    folded_points.add((x, new_y))
                else:
                    folded_points.add((x,y))
        points = folded_points

    return folded_points

def visualize_points(points):
    board = [[' '] * 50 for _ in range(50)]
    for x,y in points:
        board[x][y] = 'X'

    for row in board:
        print(row)
points = origami2()
visualize_points(points)