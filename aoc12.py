from collections import defaultdict, deque
def passage():
    file = open('/Users/ileenf/CS/aoc/aoc12.txt')

    neighbors = defaultdict(list)

    for line in file:
        line = line.strip().split('-')
        neighbors[line[0]].append(line[1])
        if line[0] != 'start' and line[1] != 'end':
            neighbors[line[1]].append(line[0])

    paths = 0

    print(neighbors)

    queue = deque()
    connected = neighbors['start']
    for node in connected:
        if node.islower():
            queue.append([node, [node], [node]])
        else:
            queue.append([node, [], [node]])

    while queue:
        connected = queue.popleft()
        node = connected[0]
        smalls = connected[1]
        lst = connected[2]
        if len(set(smalls)) != len(smalls) or node == 'start':
            continue
        if node == 'end':
            paths += 1
            print(lst)
        elif node != 'end':
            connected = neighbors[node]
            for node in connected:
                if not node.islower() or node == 'end':
                    queue.append([node, smalls, lst + [node]])
                else:
                    queue.append([node, smalls + [node], lst + [node]])
    return paths
def check_valid(lst):
    count = defaultdict(int)
    for node in lst:
        if node.islower():
            count[node] += 1

    smalls = 0
    for node, occur in count.items():
        if occur > 2:
            return False
        elif occur == 2:
            smalls += 1
    return smalls <= 1

def passage2():
    file = open('/Users/ileenf/CS/aoc/aoc12.txt')

    neighbors = defaultdict(list)

    for line in file:
        line = line.strip().split('-')
        neighbors[line[0]].append(line[1])
        if line[0] != 'start' and line[1] != 'end':
            neighbors[line[1]].append(line[0])

    paths = 0


    queue = deque()
    connected = neighbors['start']
    for node in connected:
        if node.islower():
            queue.append([node, [node], [node]])
        else:
            queue.append([node, [], [node]])

    while queue:
        connected = queue.popleft()
        node = connected[0]
        smalls = connected[1]
        lst = connected[2]
        if not check_valid(smalls) or node == 'start':
            continue
        if node == 'end':
            paths += 1
        elif node != 'end':
            connected = neighbors[node]
            for node in connected:
                if not node.islower() or node == 'end':
                    queue.append([node, smalls, lst + [node]])
                else:
                    queue.append([node, smalls + [node], lst + [node]])
    return paths

print(passage2())

