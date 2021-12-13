def binary_diag():
    file = open('/Users/ileenf/CS/aoc/aoc3.txt')

    counts = [[0,0] for i in range(12)]

    for line in file:
        line = line.strip()
        for i in range(12):
            if line[i] == '0':
                counts[i][0] += 1
            else:
                counts[i][1] += 1
    file.close()
    gamma = ''
    epsilon = ''

    for count in counts:
        zeros = count[0]
        ones = count[1]

        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)

    return gamma * epsilon

def get_most_common(arr, idx):
    zeros = 0
    ones = 0

    for line in arr:
        if line[idx] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        return '1'
    return '0'


def get_least_common(arr, idx):
    zeros = 0
    ones = 0

    for line in arr:
        if line[idx] == '0':
            zeros += 1
        else:
            ones += 1
    if ones < zeros:
        return '1'
    return '0'

def binary_diag2():
    file = open('/Users/ileenf/CS/aoc/aoc3.txt')

    zeros = 0
    ones = 0

    for line in file:
        line = line.strip()
        if line[0] == '0':
            zeros += 1
        else:
            ones += 1

    oxygen = []
    co2 = []

    file.close()
    file = open('/Users/ileenf/CS/aoc/aoc3.txt')
    for line in file:
        line = line.strip()

        if ones >= zeros:
            if line[0] == '1':
                oxygen.append(line)
            else:
                co2.append(line)
        else:
            if line[0] == '0':
                oxygen.append(line)
            else:
                co2.append(line)

    print(oxygen)
    print(co2)
    i = 1
    while len(oxygen) > 1:
        most_common = get_most_common(oxygen, i)

        temp_oxygen = []
        for bin in oxygen:
            if bin[i] == most_common:
                temp_oxygen.append(bin)

        oxygen = temp_oxygen
        i += 1

    i = 1
    while len(co2) > 1:
        least_common = get_least_common(co2, i)
        temp_co2 = []
        for bin in co2:
            if bin[i] == least_common:
                temp_co2.append(bin)

        co2 = temp_co2
        i += 1
    print(oxygen)
    print(co2)
    return int(oxygen[0], 2) * int(co2[0], 2)

print(binary_diag2())


