from collections import defaultdict
def hydro():
    file = open('/Users/ileenf/CS/aoc/aoc5.txt')

    occurences = defaultdict(int)

    for line in file:
        points = line.split('->')
        point1 = points[0].split(',')
        point2 = points[1].strip().split(',')

        x1 = int(point1[0])
        y1 = int(point1[1])
        x2 = int(point2[0])
        y2 = int(point2[1])

        if x1 == x2 and y1 != y2:
            less = min(y1,y2)
            bigger = max(y1,y2)
            while less <= bigger:
                occurences[(x1, less)] += 1
                less += 1

        elif y1 == y2 and x1 != x2:
            less = min(x1, x2)
            bigger = max(x1, x2)
            while less <= bigger:
                occurences[(less, y1)] += 1
                less += 1
        else:
            continue

    count = 0
    for point, occur in occurences.items():
        if occur >= 2:
            count += 1
    return count

def hydro2():
    file = open('/Users/ileenf/CS/aoc/aoc5.txt')

    occurences = defaultdict(int)

    for line in file:
        points = line.split('->')
        point1 = points[0].split(',')
        point2 = points[1].strip().split(',')

        x1 = int(point1[0])
        y1 = int(point1[1])
        x2 = int(point2[0])
        y2 = int(point2[1])

        if x1 == x2 and y1 != y2:
            less = min(y1,y2)
            bigger = max(y1,y2)
            while less <= bigger:
                occurences[(x1, less)] += 1
                less += 1

        elif y1 == y2 and x1 != x2:
            less = min(x1, x2)
            bigger = max(x1, x2)
            while less <= bigger:
                occurences[(less, y1)] += 1
                less += 1
        else:
            if x1 > x2 and y1 < y2:
                start_x = x1
                start_y = y1
                end_x = x2
                end_y = y2

                right_to_left = True

            elif x1 < x2 and y1 > y2:
                start_x = x2
                start_y = y2
                end_x = x1
                end_y = y1

                right_to_left = True

            elif x1 < x2 and y1 < y2:
                start_x = x1
                start_y = y1
                end_x = x2
                end_y = y2
                right_to_left = False

            elif x1 > x2 and y1 > y2:
                start_x = x2
                start_y = y2
                end_x = x1
                end_y = y1
                right_to_left = False

            if right_to_left:
                while start_x >= end_x and start_y <= end_y:
                    occurences[(start_x, start_y)] += 1
                    start_x -= 1
                    start_y += 1
            else:
                while start_x <= end_x and start_y <= end_y:
                    occurences[(start_x, start_y)] += 1
                    start_x += 1
                    start_y += 1

    count = 0
    for point, occur in occurences.items():
        if occur >= 2:
            count += 1
    return count

print(hydro2())