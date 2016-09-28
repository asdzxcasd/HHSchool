import numpy as np
from problem1 import solve


def compare(file1, file2):
    return list(map(int, file1.readlines())) == list(map(int, file2.readlines()))

def generate_test():
    a = np.zeros((50, 50))
    for i in range(12):
        a[:,i*4:i*4+3] = 5

    for i in range(6):
        a[0:3,i*8+3] = 5
        a[-3:,i*8+7] = 5

    for i in range(12):
        a[1:-1,i*4+1] = 3

    for i in range(6):
        a[1,i*8+2:i*8+5] = 3
        a[-2,i*8+6:i*8+9] = 3

    with open('temp.txt', 'wb') as f:
        np.savetxt(f, a, fmt='%.0f')


def main():
    with open('input.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            solve(input, output)
    with open('output.txt', 'rt') as output:
        with open('answers.txt', 'rt') as answers:
            if compare(output, answers):
                print('Success')
            else:
                print('Wrong output!')


if __name__ == '__main__':
    main()