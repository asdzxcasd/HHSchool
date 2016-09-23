import sys
import math


def solve_fast(num):
    str_num = str(num)
    for ln in range(1, len(str_num) + 1):  # length of solution cannot exceed length of num
        # select split point
        min_index = math.inf
        for s in range(0, ln):
            tail = str_num[:s]
            head = str_num[s:ln]
            if head[0] == '0':
                continue  # number cannot start with zero
            if s == 0:
                tail_next = ''
            else:
                tail_next = str(int(tail) + 1)
            tail_next = tail_next[-s:]  # process overflow
            pos = head + tail_next
            # verify hypothesis that num can be generated from numbers pos-1, pos, pos+1, ...
            accum = tail
            counter = int(pos)
            while len(accum) < len(str_num):
                accum += str(counter)
                counter += 1
            if accum[:len(str_num)] == str_num:
                # compute index in string from pos
                index = 0
                for i in range(1, ln):
                    index += i * (pow(10, i) - pow(10, i - 1))
                index += ln * (int(pos) - pow(10, ln - 1))
                index -= s
                min_index = min(min_index, index)
        if min_index < math.inf:
            return min_index + 1  # indexing starts from 1


def solve_simple(num):
    text = ''.join(map(str, range(1, num + 1)))
    return text.find(str(num)) + 1  # indexing starts from 1


def process_input():
    for line in sys.stdin.readlines():
        print(solve_simple(int(line)))


def compare_solutions(max_num):
    ok = True
    for num in range(1, max_num):
        solution_simple = solve_simple(num)
        solution_fast = solve_fast(num)
        if solution_simple != solution_fast:
            print("Solutions differ!")
            print(num, solution_simple, solution_fast)
            ok = False
            break
    if ok:
        print("Success")


def main():
    # process_input()
    compare_solutions(100)
    # compare_solutions(10000)


if __name__ == "__main__":
    main()
