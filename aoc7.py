import statistics
def crab1():
    file = open('/Users/ileenf/CS/aoc/aoc7.txt')

    fuel = 0

    for line in file:
        crabs = line.strip().split(',')
        crabs = [int(c) for c in crabs]
        num = statistics.median(crabs)

        for crab in crabs:
            fuel += abs(num - crab)

    return fuel

def get_fuel(num):
    count = 0
    for i in range(1,num+1):
        count += i
    return count

def crab2():
    file = open('/Users/ileenf/CS/aoc/aoc7.txt')
    fuels = []
    for line in file:
        crabs = line.strip().split(',')
        crabs = [int(c) for c in crabs]
        num = statistics.mean(crabs)
        num = round(num)

        fuel = 0
        for crab in crabs:
            fuel += get_fuel(abs(num - crab + 1))
        fuels.append(fuel)
        fuel = 0
        for crab in crabs:
            fuel += get_fuel(abs(num - crab))
        fuels.append(fuel)
        fuel = 0
        for crab in crabs:
            fuel += get_fuel(abs(num - crab-1))
        fuels.append(fuel)

    return min(fuels)
print(crab2())

