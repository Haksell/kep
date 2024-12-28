# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    grid = []
    chars = set()
    h = ir()
    for _ in range(h):
        s = input()
        grid.append(s)
        chars |= set(s)
    chars.discard(".")
    below = {c: set() for c in chars}
    for y in range(1, h):
        for x in range(20):
            c1 = grid[y - 1][x]
            c2 = grid[y][x]
            if c1 != "." and c2 != "." and c1 != c2:
                below[c1].add(c2)
    res = ""
    for _ in range(len(chars)):
        c = min(c for c, v in below.items() if len(v) == 0)
        del below[c]
        res += c
        for v in below.values():
            v.discard(c)
    print(res)


if __name__ == "__main__":
    main()
