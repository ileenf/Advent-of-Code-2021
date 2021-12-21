def in_bounds(row, col, image):
    return 0 <= row < len(image) and 0 <= col < len(image[row])


def add_border(image, border):
    border_row = [border for _ in range(len(image) + 2)]
    new_image = [border_row]
    for row in image:
        new_image.append([border] + list(row) + [border])
    new_image.append(list(border_row))

    return new_image


def count_lit_pixels(image):
    count = 0
    for row in image:
        for pixel in row:
            if pixel == '#':
                count += 1
    return count


def trench():
    file = open('/Users/ileenf/CS/aoc/aoc20.txt')
    lines = file.readlines()

    algorithm = lines[0].strip()

    image = []

    for line in lines[2:]:
        row = [p for p in line.strip()]
        image.append(row)

    curr_border = '.'
    image = add_border(image, curr_border)

    for i in range(50):
        temp_image = []

        for r in range(len(image)):
            temp_row = []
            for c in range(len(image[r])):
                bin_value = ''
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    row = dr + r
                    col = dc + c

                    if not in_bounds(row, col, image):
                        bin_value += '0' if curr_border == '.' else '1'
                    else:
                        bin_value += '0' if image[row][col] == '.' else '1'

                idx = int(bin_value, 2)
                val = algorithm[idx]
                temp_row.append(val)
            temp_image.append(temp_row)

        if curr_border == '.':
            curr_border = algorithm[0]
        elif curr_border == '#':
            curr_border = algorithm[-1]
        image = add_border(temp_image, curr_border)

    lit_pixels = count_lit_pixels(image)
    print(lit_pixels)


trench()
