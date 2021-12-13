def sonar_sweep():
    file = open('/Users/ileenf/CS/aoc/aoc1.txt')

    prev = 149
    count = 0
    for line in file:
        line = int(line.strip())
        if line > prev:
            count += 1

        prev = line

    return count

def sonar_sweep2():
    file = open('/Users/ileenf/CS/aoc/aoc1.txt')

    lines = []
    for line in file:
        lines.append(int(line.strip()))

    windows = []

    for i in range(len(lines)):
        temp = []
        if i + 3 <= len(lines):
            for j in range(i, i+3):
                temp.append(lines[j])
            windows.append(temp)
    print(windows)

    count = 0
    for i in range(len(windows)-1):
        if sum(windows[i+1]) > sum(windows[i]):
            count += 1
    return count
                     
print(sonar_sweep2())
