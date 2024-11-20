# ruff: noqa: E731
from heapq import heappop, heappush
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    arrs = []
    h = []
    for i, line in enumerate(sys.stdin):
        if i & 1:
            arr = list(map(int, line.split()))
            arrs.append(arr)
            heappush(h, (arr[0], i >> 1, 0))

    res = []
    while h:
        n, arr_idx, idx = heappop(h)
        res.append(n)
        arr = arrs[arr_idx]
        idx += 1
        if idx < len(arr):
            heappush(h, (arr[idx], arr_idx, idx))
    print(*res)


if __name__ == "__main__":
    main()
