def segment():
    file = open('/Users/ileenf/CS/aoc/aoc8.txt')
    count = 0
    for line in file:
        arr = line.split('|')
        print(arr)
        line = arr[1]

        words = line.split()

        for word in words:
            if len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7:
                count += 1

    return count

def segment2():
    file = open('/Users/ileenf/CS/aoc/aoc8.txt')
    total = 0
    word_sums_dict = {'234567': "0", '27': "1", '12356': "2", '12367': "3", '1247': "4",
                      '13467': "5", '134567': "6", '237': "7", '1234567': "8", '123467': "9" }

    for line in file:
        arr = line.split('|')
        signal = arr[0].split()
        segments = arr[1].split()

        positions = {}
        positions2 = {}
        positions3 = {}
        positions4 = {}
        seen = set()
        signal.sort(key = lambda x: len(x))

        for word in signal:
            if len(word) == 2:
                positions[word[0]] = 2
                positions[word[1]] = 7
                positions2[word[0]] = 2
                positions2[word[1]] = 7
                positions3[word[0]] = 7
                positions3[word[1]] = 2
                positions4[word[0]] = 7
                positions4[word[1]] = 2
                seen.add(word[0])
                seen.add(word[1])
            elif len(word) == 3:
                for ch in word:
                    if ch not in seen:
                        positions[ch] = 3
                        positions2[ch] = 3
                        positions3[ch] = 3
                        positions4[ch] = 3
                        seen.add(ch)
                        break

            elif len(word) == 4:
                not_seen = []
                for ch in word:
                    if ch not in seen:
                        not_seen.append(ch)
                        seen.add(ch)
                ch1 = not_seen[0]
                ch2 = not_seen[1]

                positions[ch1] = 1
                positions[ch2] = 4
                positions2[ch1] = 4
                positions2[ch2] = 1
                positions3[ch1] = 1
                positions3[ch2] = 4
                positions4[ch1] = 4
                positions4[ch2] = 1


            elif len(word) == 6:
                word_sum = ''
                not_seen = ''

                for ch in word:
                    if ch in seen:
                        word_sum += str(positions[ch])
                    else:
                        not_seen = ch
                word_sum = ''.join(sorted(word_sum))
                if word_sum == '12347':
                    positions[not_seen] = 6
                    positions2[not_seen] = 6
                    positions3[not_seen] = 6
                    positions4[not_seen] = 6
                    seen.add(not_seen)

                word_sum = ''
                not_seen = ''

                for ch in word:
                    if ch in seen:
                        word_sum += str(positions2[ch])
                    else:
                        not_seen = ch
                word_sum = ''.join(sorted(word_sum))
                if word_sum == '12347':
                    positions[not_seen] = 6
                    positions2[not_seen] = 6
                    positions3[not_seen] = 6
                    positions4[not_seen] = 6
                    seen.add(not_seen)

            elif len(word) == 7:
                for ch in word:
                    if ch not in seen:
                        positions[ch] = 5
                        positions2[ch] = 5
                        positions3[ch] = 5
                        positions4[ch] = 5
                        break

        value = ''
        for word in segments:
            curr_sum1 = ''
            curr_sum2 = ''
            curr_sum3 = ''
            curr_sum4 = ''
            for ch in word:
                curr_sum1 += str(positions[ch])
                curr_sum2 += str(positions2[ch])
                curr_sum3 += str(positions3[ch])
                curr_sum4 += str(positions4[ch])
            curr_sum1 = ''.join(sorted(curr_sum1))
            curr_sum2 = ''.join(sorted(curr_sum2))
            curr_sum3 = ''.join(sorted(curr_sum3))
            curr_sum4 = ''.join(sorted(curr_sum4))
            if curr_sum1 in word_sums_dict:
                num = word_sums_dict[curr_sum1]
            elif curr_sum2 in word_sums_dict:
                num = word_sums_dict[curr_sum2]
            elif curr_sum3 in word_sums_dict:
                num = word_sums_dict[curr_sum3]
            elif curr_sum4 in word_sums_dict:
                num = word_sums_dict[curr_sum4]
            value += num

        total += int(value)
    return total

print(segment2())











