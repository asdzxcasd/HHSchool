import sys
import math


def solve_fast(num):
    for ln in range(1, len(num) + 1):  # length of solution cannot exceed length of num
        # select split point
        min_index = math.inf
        for s in range(0, ln):
            tail = num[:s]
            head = num[s:ln]
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
            while len(accum) < len(num):
                accum += str(counter)
                counter += 1
            if accum[:len(num)] == num:
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
    text = ''.join(map(str, range(1, pow(10, len(num)) + 1)))
    # text = ''.join(map(str, range(1, int(num) + 1)))
    return text.find(num) + 1  # indexing starts from 1


def process_input():
    for line in sys.stdin.readlines():
        print(solve_simple(line))


def compare_solutions(solver1, solver2, max_num):
    ok = True
    for num in map(str, range(1, max_num)):
        answer1 = solver1(num)
        answer2 = solver2(num)
        if answer1 != answer2:
            print("Solutions differ!")
            print(num, answer1, answer2)
            ok = False
            break
    if ok:
        print("Success")


def run_tests(solver):
    def test(number, expected_answer):
        received_answer = solver(number)
        if (received_answer != expected_answer):
            print('Test failed!')
            print('number: {}, expected: {}, received {}'.format(number, expected_answer, received_answer))
    test('1', 1)
    test('0', 11)
    test('02', 31)
    test('00', 191)
    test('90', 170)
    test('991', 188)
    test('9100', 189)
    test('6789', 6)
    test('111', 12)


def main():
    # process_input()
    # compare_solutions(solve_simple, solve_fast, 100)
    # compare_solutions('10000')
    run_tests(solve_simple)
    run_tests(solve_fast)


if __name__ == "__main__":
    main()
