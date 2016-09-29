import numpy as np

from problem1 import solve, solve_test_case


def compare(file1, file2):
    return list(map(int, file1.readlines())) == list(map(int, file2.readlines()))


def generate_test():
    a = np.zeros((50, 50))
    for i in range(12):
        a[:, i * 4:i * 4 + 3] = 5

    for i in range(6):
        a[0:3, i * 8 + 3] = 5
        a[-3:, i * 8 + 7] = 5

    for i in range(12):
        a[1:-1, i * 4 + 1] = 3

    for i in range(6):
        a[1, i * 8 + 2:i * 8 + 5] = 3
        a[-2, i * 8 + 6:i * 8 + 9] = 3

    with open('temp.txt', 'wb') as f:
        np.savetxt(f, a, fmt='%.0f')


def test_symmetry():
    ok = True
    np.random.seed(12345)
    for i in range(50):
        n = np.random.randint(1, 50 + 1)
        m = np.random.randint(1, 50 + 1)
        a = np.random.randint(1, 1000 + 1, (n, m))
        ans1 = solve_test_case(n, m, a)
        ans2 = solve_test_case(m, n, a.transpose())
        if ans1 != ans2:
            print('Answers are different!')
            ok = False
    if ok:
        print('Test symmetry: success')


def run_tests():
    with open('input.txt', 'rt') as in_stream:
        with open('output.txt', 'wt') as out_stream:
            solve(in_stream, out_stream)
    with open('output.txt', 'rt') as out_stream:
        with open('answers.txt', 'rt') as ans_stream:
            if compare(out_stream, ans_stream):
                print('Run tests: success')
            else:
                print('Wrong output!')


def main():
    test_symmetry()
    run_tests()


if __name__ == '__main__':
    main()
