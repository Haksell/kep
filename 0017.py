# ruff: noqa: E731, E741
import sys
from functools import wraps
from time import time

sys.setrecursionlimit(10000)

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def timing(f):
    @wraps(f)
    def wrap():
        ts = time()
        result = f()
        te = time()
        print(f"{f.__name__}() took {te - ts:.6f}s.", file=sys.stderr)
        return result

    return wrap


@timing
def naive():
    res = " ".join(
        i for i in map(str, range(10**3, 10**4)) if sum(map(ord, i)) & 1 == 0
    )
    print("".join(res)[:100])


@timing
def smart():
    def helper(a, b, c, d):
        nonlocal i, res
        if a >= 10:
            return
        if b >= 10:
            helper(a + 1, 0, 0, ~a & 1)
            return
        if c >= 10:
            helper(a, b + 1, 0, (a ^ b) & 1)
            return
        if d >= 10:
            helper(a, b, c + 1, ~(a ^ b ^ c) & 1)
            return
        res[i] = a ^ 48
        res[i + 1] = b ^ 48
        res[i + 2] = c ^ 48
        res[i + 3] = d ^ 48
        i += 5
        helper(a, b, c, d + 2)

    i = 0
    res = [32] * (4500 * 5 - 1)
    helper(1, 0, 0, 1)
    print(bytearray(res).decode("ascii")[:100])


def main():
    naive()
    smart()


if __name__ == "__main__":
    main()
