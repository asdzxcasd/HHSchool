import heapq
import sys
import numpy as np


def dijkstra(ground, y0, x0):
    # fill the island starting from outside
    (n, m) = ground.shape
    water = ground.copy()
    u = np.zeros((n, m), dtype=bool)
    q = []
    u[y0, x0] = True
    heapq.heappush(q, (water[y0, x0], (y0, x0)))
    dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while len(q) > 0:
        (_, (y, x)) = heapq.heappop(q)
        for d in dv:
            (y2, x2) = (y + d[0], x + d[1])
            if y2 >= 0 and x2 >= 0 and y2 < n and x2 < m:
                if ~u[y2, x2]:
                    if (water[y2, x2] < water[y, x]):
                        water[y2, x2] = water[y, x]
                    u[y2, x2] = True
                    heapq.heappush(q, (water[y2, x2], (y2, x2)))
    return np.sum(water - ground)


def solve(input, output):
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
        print(dijkstra(b, 0, 0), file=output)


def main():
    solve(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
