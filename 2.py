import sys

def solve_simple(num):
    text = ''.join(map(str, range(1, num+1)))
    return text.find(str(num)) + 1

def process_input():
    for line in sys.stdin.readlines():
        print(solve_simple(int(line)))

def main():
    process_input()

if __name__ == "__main__":
    main()
