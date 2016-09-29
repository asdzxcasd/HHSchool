import sys


def index_from_pos(pos):
    index = 0
    for i in range(1, len(pos)):
        index += i * (pow(10, i) - pow(10, i - 1))
    index += len(pos) * (int(pos) - pow(10, len(pos) - 1))
    return index + 1  # indexing starts from 1


def solve_fast(num):
    if num == '0' * len(num):
        return index_from_pos('1' + num) + 1  # start from second digit of 100...0
    for ln in range(1, len(num) + 1):  # length of solution cannot exceed length of num, except of all zeros
        # select split point
        min_index = float('inf')
        for s in range(0, ln):
            tail = num[:s]
            head = num[s:ln]
            if head[0] == '0':
                continue  # number cannot start with zero
            if s == 0:
                tail_next = ''
            else:
                tail_next = str(int(tail) + 1).zfill(s)
            tail_next = tail_next[-s:]  # handle overflow
            pos = head + tail_next
            # verify hypothesis that num can be generated from numbers pos-1, pos, pos+1, ...
            accum = tail
            counter = int(pos)
            while len(accum) < len(num):
                accum += str(counter)
                counter += 1
            if accum[:len(num)] == num:
                index = index_from_pos(pos) - s
                min_index = min(min_index, index)
        if min_index < float('inf'):
            return min_index


def process_input():
    for line in sys.stdin.read().splitlines():
        print(solve_fast(line))


def main():
    process_input()


if __name__ == "__main__":
    main()
