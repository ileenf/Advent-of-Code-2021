

def flash():
    def dfs(row, col, octopus, seen):
        nonlocal adjacent_flashes
        adjacent_flashes += 1
        octopus[row][col] = 0
        seen.add((row,col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r = dr + row
            c = dc + col

            if r >= 0 and r < len(octopus) and c >= 0 and c < len(octopus[0]) and (r,c) not in seen:
                octopus[r][c] += 1
                if octopus[r][c] > 9:
                    dfs(r, c, octopus, seen)

    file = open('/Users/ileenf/CS/aoc/aoc11.txt')

    octopus = []

    for line in file:
        line = line.strip()
        arr = [int(l) for l in line]
        octopus.append(arr)

    flashes = 0

    for i in range(100):
        seen = set()
        for row in range(len(octopus)):
            for col in range(len(octopus[row])):
                octopus[row][col] += 1

        for row in range(len(octopus)):
            for col in range(len(octopus[row])):

                if octopus[row][col] > 9:

                    adjacent_flashes = 0
                    dfs(row, col, octopus, seen)
                    flashes += adjacent_flashes


    return flashes

def check_all_flashing(octopus):
    for row in range(len(octopus)):
        for col in range(len(octopus[row])):
            if octopus[row][col] != 0:
                return False
    return True
def flash2():
    def dfs(row, col, octopus, seen):
        octopus[row][col] = 0
        seen.add((row,col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r = dr + row
            c = dc + col

            if r >= 0 and r < len(octopus) and c >= 0 and c < len(octopus[0]) and (r,c) not in seen:
                octopus[r][c] += 1
                if octopus[r][c] > 9:
                    dfs(r, c, octopus, seen)

    file = open('/Users/ileenf/CS/aoc/aoc11.txt')

    octopus = []

    for line in file:
        line = line.strip()
        arr = [int(l) for l in line]
        octopus.append(arr)

    i = 0
    while True:
        seen = set()
        for row in range(len(octopus)):
            for col in range(len(octopus[row])):
                octopus[row][col] += 1

        for row in range(len(octopus)):
            for col in range(len(octopus[row])):

                if octopus[row][col] > 9:

                    dfs(row, col, octopus, seen)
        i += 1
        if check_all_flashing(octopus):
            return i


print(flash2())