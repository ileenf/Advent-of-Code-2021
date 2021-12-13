from collections import defaultdict
def lanternfish():
    file = open('/Users/ileenf/CS/aoc/aoc6.txt')

    fishes = []
    for line in file:
        line = line.strip().split(',')
        fishes = [int(f) for f in line]
        day = 1

        while day <= 80:
            temp_fishes = []
            for fish in fishes:
                if fish == 0:
                    temp_fishes.append(6)
                    temp_fishes.append(8)
                else:
                    temp_fishes.append(fish-1)

            fishes = temp_fishes

            print(day)
            day += 1

    return len(fishes)

def lanternfish2():
    file = open('/Users/ileenf/CS/aoc/aoc6.txt')

    fishes = defaultdict(int)
    for line in file:
        line = line.strip().split(',')
        for f in line:
            fishes[int(f)] += 1
        day = 1


        while day <= 256:
            copy_fishes = defaultdict(int)
            for fish, count in fishes.items():
                if fish == 0:
                    copy_fishes[6] += count
                    copy_fishes[8] += count
                else:
                    copy_fishes[fish - 1] += count

            day += 1
            print(day)
            fishes = copy_fishes

    return sum(fishes.values())


print(lanternfish2())
