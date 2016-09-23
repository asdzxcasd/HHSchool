import sys
import math


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
        min_index = math.inf
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
        if min_index < math.inf:
            return min_index


def solve_simple(num):
    text = ''.join(map(str, range(1, pow(10, len(num)) + 1)))
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
        print("Compare solutions: success")


def run_tests(solver):
    def test(number, expected_answer):
        received_answer = solver(number)
        if received_answer != expected_answer:
            print('Test failed!')
            print('number: {}, expected: {}, received {}'.format(number, expected_answer, received_answer))

    test('1', 1)
    test('0', 11)
    test('02', 31)
    test('00', 191)
    test('001', 191)
    test('000', 2891)
    test('90', 170)
    test('991', 188)
    test('9100', 189)
    test('6789', 6)
    test('111', 12)
    test('99', index_from_pos('89') + 1)
    test('999', index_from_pos('899') + 1)
    test('99999', index_from_pos('89999') + 1)
    test('99999999999999999999999999999999999999999999999999',
         index_from_pos('89999999999999999999999999999999999999999999999999') + 1)
    test('00000000000000000000000000000000000000000000000000',
         index_from_pos('100000000000000000000000000000000000000000000000000') + 1)
    test('00000000000000000000000000000000000000000000000000', 4988888888888888888888888888888888888888888888888891)
    test('12345678910111213141516171819202122232425262728293', 1)


def test_sequence(solver, max_pos, max_len):
    seq = ''.join(map(str, range(1, max_pos + 1)))
    ok = True
    for i in range(len(seq)):
        for ln in range(1, max_len):
            if i + ln < len(seq):
                subseq = seq[i:i + ln]
                expected_answer = i + 1
                received_answer = solver(subseq)
                i2 = received_answer - 1
                if (received_answer > expected_answer or
                                received_answer < expected_answer and seq[i2:i2 + ln] != subseq):
                    print('Test failed!')
                    print('number: {}, expected: {}, received {}'.format(subseq, expected_answer, received_answer))
                    ok = False
    if ok:
        print('Test sequence: success')


def main():
    # process_input()
    # compare_solutions(solve_simple, solve_fast, 1000)
    # run_tests(solve_simple)
    # run_tests(solve_fast)
    # test_sequence(solve_simple, 100, 5)
    test_sequence(solve_fast, 1000, 50)
    # test_sequence(solve_fast, 10000, 10)


if __name__ == "__main__":
    main()
