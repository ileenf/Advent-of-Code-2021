def basin():
    file = open('/Users/ileenf/CS/aoc/tester.txt')

    map = []
    lowest = []

    for line in file:
        line = line.strip()
        heights = [int(h) for h in line]
        map.append(heights)


    for row in range(len(map)):
        for col in range(len(map[row])):
            curr_val = map[row][col]
            adjacent = []
            for r, c in [(0,1), (0,-1), (1,0), (-1,0)]:
                dr = row + r
                dc = col + c
                if dr >= 0 and dr < len(map) and dc >= 0 and dc < len(map[row]):
                    adjacent.append(map[dr][dc])

            if curr_val < min(adjacent):
                lowest.append(curr_val)

    count = sum(lowest) + len(lowest)
    return count




def basin2():
    file = open('/Users/ileenf/CS/aoc/aoc9.txt')

    map = []
    lowest = set()

    for line in file:
        line = line.strip()
        heights = [int(h) for h in line]
        map.append(heights)


    for row in range(len(map)):
        for col in range(len(map[row])):
            curr_val = map[row][col]
            adjacent = []
            for r, c in [(0,1), (0,-1), (1,0), (-1,0)]:
                dr = row + r
                dc = col + c
                if dr >= 0 and dr < len(map) and dc >= 0 and dc < len(map[row]):
                    adjacent.append(map[dr][dc])

            if curr_val < min(adjacent):
                lowest.add((row,col))

    def dfs(dr, dc, map, seen):
        seen.add((dr, dc))
        nonlocal count
        count += 1
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r = dr + dir[0]
            c = dc + dir[1]
            if r >= 0 and r < len(map) and c >= 0 and c < len(map[0]) and map[r][c] != 9 and (r, c) not in seen and map[r][c] > map[dr][dc]:
                dfs(r, c, map, seen)

    largest = []
    seen = set()
    for row in range(len(map)):
        for col in range(len(map[row])):
            if (row, col) in lowest:
                count = 0
                dfs(row, col, map, seen)
                size = count
                largest.append(size)
    largest.sort()
    return largest[-1] * largest[-2] * largest[-3]

print(basin2())


