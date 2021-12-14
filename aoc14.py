from collections import defaultdict
import math
def polymer():
    file = open('/Users/ileenf/CS/aoc/tester.txt')

    template = ''
    mapping = {}
    i = 0
    for line in file:
        if i == 0:
            template = line.strip()

        elif line.strip() == '':
            continue

        else:
            pair = line.strip().split('->')
            mapping[pair[0].strip()] = pair[1].strip()
        i += 1

    for _ in range(10):
        new_template = ''
        for i in range(len(template)-1):
            chars = template[i] + template[i+1]
            if chars in mapping:
                middle_char = mapping[chars]
                if i == 0:
                    new_template += (template[i] + middle_char + template[i+1])
                elif i == len(template)-2:
                    new_template += (middle_char + template[i + 1])
                else:
                    new_template += (middle_char + template[i+1])
            else:
                new_template += chars
        template = new_template

    most_common = max(template, key = lambda x: template.count(x))
    least_common = min(template, key = lambda x: template.count(x))

    print(template.count(most_common) - template.count(least_common))


def polymer2():
    file = open('/Users/ileenf/CS/aoc/aoc14.txt')

    template = ''
    mapping = {}
    i = 0
    for line in file:
        if i == 0:
            template = line.strip()

        elif line.strip() == '':
            continue

        else:
            pair = line.strip().split('->')
            mapping[pair[0].strip()] = pair[1].strip()
        i += 1

    template_dict = defaultdict(int)
    occurences = defaultdict(int)

    for i in range(len(template) - 1):
        chars = template[i] + template[i+1]
        template_dict[chars] += 1

    for ch in template:
        occurences[ch] += 1

    for j in range(40):
        new_template = defaultdict(int)
        for chars, count in template_dict.items():
            middle_char = mapping[chars]
            new_template[chars[0] + middle_char] += count
            new_template[middle_char + chars[1]] += count

            occurences[middle_char] += count

        template_dict = new_template

    print(max(occurences.values())-min(occurences.values()))

polymer2()