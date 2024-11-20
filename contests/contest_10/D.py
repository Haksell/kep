# ruff: noqa: E731, E741
import re
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    t = "00/00/0000"
    s = input()
    s += t[len(s) :]
    print("YES" if re.fullmatch(r"\d\d/\d\d/\d\d\d\d", s) else "No")


if __name__ == "__main__":
    main()
