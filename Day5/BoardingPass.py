import math


def read_file(path):
    ret = []
    with open(path, 'r') as input:
        for line in input:
            ret.append([c for c in line.strip()])
    return ret


def determine_row(low, high, string, low_op, high_op):
    op = string[0]
    if len(string) == 1:
        if op == high_op:
            return high
        else:
            return low
    else:
        count = (high - low) + 1
        lower_high = low + (math.floor(count / 2)) - 1
        higher_low = low + (math.ceil(count / 2))
        if op == high_op:
            return determine_row(higher_low, high, string[1:], low_op, high_op)
        else:
            return determine_row(low, lower_high, string[1:], low_op, high_op)


def board(path):
    strings = read_file(path)
    passes = []
    for string in strings:
        row = determine_row(0, 127, string[:7], 'F', 'B')
        col = determine_row(0, 7, string[7:], 'L', 'R')
        passes.append((row * 8) + col)
    passes.sort()
    previous_id = None
    for i in passes:
        if previous_id is None:
            previous_id = i
        else:
            diff = i - previous_id
            previous_id = i
            if diff > 1:
                return i - 1
    return 0


print(board('input.txt'))
