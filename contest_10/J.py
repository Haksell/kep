# ruff: noqa: E731, E741
from itertools import combinations, product
from random import randint, randrange
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def miller_rabin(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(50):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def solve(n):
    n = list(map(int, str(n)))
    for ops in range(min(2, len(n)) + 1):
        for idx in combinations(list(range(len(n))), r=ops):
            for digits in product(list(range(10)), repeat=ops):
                a = n.copy()
                for i, d in zip(idx, digits):
                    a[i] = d
                a = int("".join(map(str, a)))
                if miller_rabin(a):
                    print(ops)
                    for i, d in zip(idx, digits):
                        print(i + 1, d)
                    return
    print(-1)


def main():
    if False:
        for _ in range(1000):
            n = randint(1, 10**50)
            print(n)
            solve(n)
            print("===========")
    else:
        n = int(input())
        solve(n)


if __name__ == "__main__":
    main()
