def dive():
    file = open('/Users/ileenf/CS/aoc/aoc2.txt')
    horiz = 0
    depth = 0
    for line in file:
        lst = line.strip().split()

        dir = lst[0]
        dist = int(lst[1])

        if dir == "forward":
            horiz += dist
        elif dir == "down":
            depth += dist
        else:
            depth -= dist

    return horiz * depth


def dive2():
    file = open('/Users/ileenf/CS/aoc/aoc2.txt')
    horiz = 0
    depth = 0
    aim = 0
    for line in file:
        lst = line.strip().split()

        dir = lst[0]
        dist = int(lst[1])

        if dir == "forward":
            horiz += dist
            depth += (aim * dist)
        elif dir == "down":
            aim += dist
        else:
            aim -= dist

    return horiz * depth

print(dive2())