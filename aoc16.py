import math

i = 0
def parse(bin_str):
    global i
    version = int(bin_str[i:i + 3], 2)

    i += 3
    packet_id = int(bin_str[i:i + 3], 2)
    version_sum = 0
    i += 3

    if packet_id == 4:
        literal = ''

        while bin_str[i] != '0':
            literal += bin_str[i + 1:i + 5]
            i += 5

        literal += bin_str[i + 1:i + 5]
        i += 5
        literal = int(literal, 2)

    else:
        length_type_id = bin_str[i]
        i += 1

        if length_type_id == '0':
            length = int(bin_str[i:i + 15], 2)
            i += 15
            curr_len = 0
            while curr_len < length:
                prev_i = i
                version_sum += parse(bin_str)
                curr_len += (i - prev_i)

        elif length_type_id == '1':
            num_sub_packets = int(bin_str[i:i + 11], 2)
            i += 11
            for _ in range(num_sub_packets):
                version_sum += parse(bin_str)
    return version_sum + version


def packet():
    file = open('/Users/ileenf/CS/aoc/aoc16.txt')
    for line in file:
        hex_string = line.strip()

    decimal_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    binary_string = ''

    for ch in hex_string:
        binary_string += decimal_to_bin[ch]

    print(parse(binary_string))


def parse2(bin_str):
    global i
    value = 0
    version = int(bin_str[i:i + 3], 2)

    i += 3
    packet_id = int(bin_str[i:i + 3], 2)
    i += 3

    if packet_id == 4:
        literal = ''

        while bin_str[i] != '0':
            literal += bin_str[i + 1:i + 5]
            i += 5

        literal += bin_str[i + 1:i + 5]
        i += 5
        literal = int(literal, 2)
        return literal

    else:
        length_type_id = bin_str[i]
        i += 1

        if length_type_id == '0':
            length = int(bin_str[i:i + 15], 2)
            i += 15
            curr_len = 0
            while curr_len < length:
                prev_i = i
                if packet_id == 0:
                    value += parse2(bin_str)
                elif packet_id == 1:
                    if curr_len == 0:
                        value = parse2(bin_str)
                    else:
                        value *= parse2(bin_str)
                elif packet_id == 2:
                    if curr_len == 0:
                        value = math.inf
                    value = min(value, parse2(bin_str))
                elif packet_id == 3:
                    if curr_len == 0:
                        value = -1
                    value = max(value, parse2(bin_str))
                elif packet_id == 5:
                    first = parse2(bin_str)
                    second = parse2(bin_str)
                    if first > second:
                        value = 1
                    else:
                        value = 0
                elif packet_id == 6:
                    first = parse2(bin_str)
                    second = parse2(bin_str)
                    if first < second:
                        value = 1
                    else:
                        value = 0
                elif packet_id == 7:
                    first = parse2(bin_str)
                    second = parse2(bin_str)
                    if first == second:
                        value = 1
                    else:
                        value = 0
                curr_len += (i - prev_i)

        elif length_type_id == '1':
            num_sub_packets = int(bin_str[i:i + 11], 2)
            i += 11
            count = 0

            while count < num_sub_packets:
                if packet_id == 0:
                    value += parse2(bin_str)
                elif packet_id == 1:
                    if count == 0:
                        value = parse2(bin_str)
                    else:
                        value *= parse2(bin_str)
                elif packet_id == 2:
                    if count == 0:
                        value = math.inf
                    value = min(value, parse2(bin_str))
                elif packet_id == 3:
                    if count == 0:
                        value = -1
                    value = max(value, parse2(bin_str))
                elif packet_id == 5:
                    first = parse2(bin_str)
                    second = parse2(bin_str)
                    count += 1

                    if first > second:
                        value = 1
                    else:
                        value = 0
                elif packet_id == 6:
                    first = parse2(bin_str)
                    second = parse2(bin_str)
                    count += 1

                    if first < second:
                        value = 1
                    else:
                        value = 0
                elif packet_id == 7:
                    first = parse2(bin_str)
                    second = parse2(bin_str)
                    count += 1

                    if first == second:
                        value = 1
                    else:
                        value = 0
                count += 1

    return value


def packet2():
    file = open('/Users/ileenf/CS/aoc/aoc16.txt')
    for line in file:
        hex_string = line.strip()

    decimal_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    binary_string = ''

    for ch in hex_string:
        binary_string += decimal_to_bin[ch]

    print(parse2(binary_string))
