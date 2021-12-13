from collections import defaultdict
def syntax():
    file = open('/Users/ileenf/CS/aoc/tester.txt')
    mapping = {')': ['(', 3], ']': ['[', 57],'}': ['{', 1197],'>': ['<', 25137]}
    count = 0

    for line in file:
        chunks = line.strip()

        stack = []
        for chunk in chunks:
            if chunk == '(' or chunk == '[' or chunk == '{' or chunk == '<':
                stack.append(chunk)
            else:
                if stack:
                    prev = stack.pop()
                    if prev != mapping[chunk][0]:
                        count += mapping[chunk][1]
                        break
    return count

def syntax2():
    file = open('/Users/ileenf/CS/aoc/aoc10.txt')
    mapping = {'(': 1, '[': 2, '{': 3, '<': 4}
    mapping2 = {')': ['(', 3], ']': ['[', 57], '}': ['{', 1197], '>': ['<', 25137]}
    counts = []

    for line in file:
        chunks = line.strip()

        corrupt = False
        stack = []
        for chunk in chunks:
            if chunk == '(' or chunk == '[' or chunk == '{' or chunk == '<':
                stack.append(chunk)
            else:
                if stack:
                    prev = stack[-1]
                    if prev == mapping2[chunk][0]:
                        stack.pop()
                    else:
                        corrupt = True
                        break
        count = 0
        if not corrupt:
            for bracket in reversed(stack):
                val = mapping[bracket]
                count = count * 5
                count += val
            counts.append(count)

    counts.sort()
    mid = len(counts) // 2


    return counts[mid]

print(syntax2())