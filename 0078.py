# ruff: noqa: E731
from datetime import datetime  # noqa: F401
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    # print(7 - datetime.now().isoweekday())
    # print(7 - datetime(year=2021, month=4, day=3).isoweekday())
    print(2)  # ???


if __name__ == "__main__":
    main()
