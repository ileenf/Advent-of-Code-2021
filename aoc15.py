import math
import heapq

# used dijkstra's algorithm
def chiton():
    file = open('/Users/ileenf/CS/aoc/aoc15.txt')
    paths = []

    for line in file:
        path = [int(num) for num in line.strip()]
        paths.append(path)

    distances = [[math.inf] * len(paths[0]) for _ in range(len(paths))]
    seen = set()
    min_distances = [[0, [0, 0]]]
    heapq.heapify(min_distances)
    distances[0][0] = 0

    while min_distances:
        min_ele = heapq.heappop(min_distances)
        row = min_ele[1][0]
        col = min_ele[1][1]
        seen.add((row, col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r = row + dr
            c = col + dc

            if 0 <= r < len(paths) and 0 <= c < len(paths[r]) and (r, c) not in seen:
                temp_dist = distances[row][col] + paths[r][c]
                if temp_dist < distances[r][c]:
                    distances[r][c] = temp_dist
                    heapq.heappush(min_distances, [temp_dist, [r, c]])

    return distances[len(paths) - 1][len(paths[0]) - 1]


# used dijkstra's algorithm
def chiton2():
    file = open('/Users/ileenf/CS/aoc/aoc15.txt')
    paths = []

    for line in file:
        path = []
        for counter in range(5):
            path += [int(num) + counter if int(num) + counter <= 9 else int(num) + counter - 9 for num in line.strip()]
        paths.append(path)

    curr_path = [list(path) for path in paths]
    for counter in range(1, 5):
        for path in curr_path:
            new_path = [int(num) + counter if int(num) + counter <= 9 else int(num) + counter - 9 for num in path]
            paths.append(new_path)

    distances = [[math.inf] * len(paths[0]) for _ in range(len(paths))]
    seen = set()
    min_distances = [[0, [0, 0]]]
    heapq.heapify(min_distances)
    distances[0][0] = 0

    while min_distances:
        min_ele = heapq.heappop(min_distances)
        row = min_ele[1][0]
        col = min_ele[1][1]
        seen.add((row, col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r = row + dr
            c = col + dc

            if 0 <= r < len(paths) and 0 <= c < len(paths[r]) and (r, c) not in seen:
                temp_dist = distances[row][col] + paths[r][c]
                if temp_dist < distances[r][c]:
                    distances[r][c] = temp_dist
                    heapq.heappush(min_distances, [temp_dist, [r, c]])

    return distances[len(paths) - 1][len(paths[0]) - 1]
