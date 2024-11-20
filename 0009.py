# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


"""
2178 <-> 8712
4 * (1000*a+100*b+10*c+d) = 1000*d+100*c+10*b+a
a = 1 or 2 otherwise too big
a = 2 because result is a multiple of 4
8000 + 4 * (100*b+10*c+d) = 1000*d+100*c+10*b+2
7998 + 4 * (100*b+10*c+d) = 1000*d+100*c+10*b
d = 8 or 9 otherwise too small
d = 8 because 4*8 ends in 2
7998 + 4 * (100*b+10*c+8) = 1000*8+100*c+10*b
7998 + 32 + 4 * (100*b+10*c) = 8000+100*c+10*b
30 + 4 * (100*b+10*c) = 100*c+10*b
3 + 4 * (10*b+c) = 10*c+b
3 + 40b + 4c = 10c + b
3 + 39b + 4c = 10c
3 + 39b = 6c
13b + 1 = 2c
b = 1
14 = 2c
c = 7
"""


def main():
    print(2178)


if __name__ == "__main__":
    main()
