import heapq
import queue
import sys
import numpy as np


def bfs(b, y0, x0):
    (n, m) = b.shape
    # c = np.zeros((n, m), dtype=int)
    c = b.copy()
    u = np.zeros((n, m), dtype=bool)
    q = []
    u[y0, x0] = True
    heapq.heappush(q, (c[y0, x0], (y0, x0)))
    dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(q) > 0:
        (_, (y, x)) = heapq.heappop(q)
        for d in dv:
            (y2, x2) = (y + d[0], x + d[1])
            if y2 >= 0 and x2 >= 0 and y2 < n and x2 < m:
                if ~u[y2, x2]:
                    if (c[y2, x2] < c[y, x]):
                        c[y2, x2] = c[y, x]
                    u[y2, x2] = True
                    heapq.heappush(q, (c[y2, x2], (y2, x2)))
        # print(u)
    # print(b)
    # print(c)
    # print()
    return np.sum(c - b)




def solve(input):
    n_tests = int(input.readline())
    for _ in range(n_tests):
        # read the matrix
        (n, m) = map(int, input.readline().split())
        a = [None] * n
        for i in range(n):
            a[i] = list(map(int, input.readline().split()))
        # extend boundaries with zeros
        b = np.zeros((n + 2, m + 2), dtype=int)
        b[1:n+1, 1:m+1] = np.array(a, dtype=int)
        print(bfs(b, 0, 0))


def main():
    # solve(sys.stdin)
    with open('input.txt', 'rt') as f:
        solve(f)


if __name__ == "__main__":
    main()
