# ruff: noqa: E731, E741
from math import prod
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


MULS = [99, 28, 10, 12, 12, 30]
OBSERVATION_BITS = prod(MULS).bit_length()

MAX_OBSERVATIONS = 100_000
FIRST_BITS = MAX_OBSERVATIONS.bit_length()


def intify(s):
    r = 0
    for i, m in enumerate(MULS):
        r *= m
        r += int(s[2 * i + 1 : 2 * i + 3]) - 1
    return r


def stringify(n):
    parts = []
    for m in reversed(MULS):
        n, part = divmod(n, m)
        parts.append(f"{part+1:02}")
    return "K" + "".join(reversed(parts))


def encrypt(ints, depth, res):
    if depth == OBSERVATION_BITS:
        return
    mask = 1 << (OBSERVATION_BITS - depth - 1)
    zero = [n for n in ints if not (n & mask)]
    one = [n for n in ints if n & mask]
    bits = len(ints).bit_length()
    res.append(f"{len(zero):0{bits}b}")
    if zero:
        encrypt(zero, depth + 1, res)
    if one:
        encrypt(one, depth + 1, res)


def decrypt(s, i, quantity, depth, value, ints):
    if depth == OBSERVATION_BITS:
        ints.extend([value] * quantity)
        return i
    bits = quantity.bit_length()
    zero = int(s[i : i + bits], 2)
    one = quantity - zero
    i += bits
    if zero:
        i = decrypt(s, i, zero, depth + 1, value << 1, ints)
    if one:
        i = decrypt(s, i, one, depth + 1, value << 1 | 1, ints)
    return i


def main():
    if ir() == 1:
        n = ir()
        ints = [intify(input()) for _ in range(n)]
        res = [f"{n:0{FIRST_BITS}b}"]
        encrypt(ints, 0, res)
        print("".join(res), end="")
    else:
        s = input()
        n = int(s[:FIRST_BITS], 2)
        ints = []
        decrypt(s, FIRST_BITS, n, 0, 0, ints)
        print(n)
        for x in ints:
            print(stringify(x))


if __name__ == "__main__":
    main()
