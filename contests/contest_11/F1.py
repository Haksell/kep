# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class FenwickTree:
    def __init__(self, size):
        self.__len = size
        self.__tree = [0] * (size + 1)
        self.__sum = 0

    @staticmethod
    def from_list(data):
        instance = FenwickTree(len(data))
        for i, n in enumerate(data, 1):
            instance.__tree[i] += n
            j = i + (i & -i)
            if j <= instance.__len:
                instance.__tree[j] += instance.__tree[i]
            instance.__sum += n
        return instance

    def __len__(self):
        return self.__len

    def __getitem__(self, i):
        return self.prefix_sum(i + 1) - self.prefix_sum(i)

    @property
    def sum(self):
        return self.__sum

    def update(self, i, delta):
        i += 1
        self.__sum += delta
        while i <= self.__len:
            self.__tree[i] += delta
            i += i & -i

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.__tree[i]
            i -= i & -i
        return res

    def suffix_sum(self, i):
        return self.__sum - self.prefix_sum(i)

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left)


def main():
    n = ir()
    h = (n + 1) >> 1
    a = lmir()
    t = c = sum(a)
    ft = FenwickTree(h)
    for i in range(h):
        ft.update(i, c)
        c -= a[i] + a[~i]
        t += c
    for _ in rir():
        k = ir()
        print(ft.prefix_sum(min(k, n - k + 1)))


if __name__ == "__main__":
    main()

"""
5
1 2 3 4 5
3
1
3
5

4
1 2 3 4
4
1
2
3
4
"""
