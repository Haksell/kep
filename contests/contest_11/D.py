# ruff: noqa: E731, E741
from collections import Counter
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_primes(n):
    s = [True] * n
    s[0] = s[1] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            for j in range(i * i, n, i):
                s[j] = False
    return s


def is_prime(primes, k):
    if k < 2:
        return False
    for p in primes:
        if p * p > k:
            return True
        if k % p == 0:
            return False


def main():
    read()
    sieve = get_primes(100_001)
    primes = [i for i, b in enumerate(sieve) if b]
    a = Counter(mir())
    for k, v in a.items():
        if sieve[v] and is_prime(primes, k):
            print(k)
            return
    print(-1)


if __name__ == "__main__":
    main()
