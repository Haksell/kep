# ruff: noqa: E731, E741
from collections import defaultdict
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


# def main():
#     levels = [dict()]
#     for _ in rir():
#         s = input()
#         if s == "{":
#             levels.append(dict())
#         elif s == "}":
#             levels.pop()
#         else:
#             k, v = s.split("=")
#             try:
#                 levels[-1][k] = int(v)
#             except ValueError:
#                 for level in reversed(levels):
#                     if v in level:
#                         levels[-1][k] = level[v]
#                         break
#                 else:
#                     levels[-1][k] = 0
#             print(levels[-1][k])


def main():
    values = defaultdict(list)
    levels = [set()]
    for _ in rir():
        s = input()
        if s == "{":
            levels.append(set())
        elif s == "}":
            for k in levels.pop():
                values[k].pop()
        else:
            k, v = s.split("=")
            try:
                p = int(v)
            except ValueError:
                p = values[v][-1] if values[v] else 0
            if k in levels[-1]:
                values[k][-1] = p
            else:
                values[k].append(p)
            levels[-1].add(k)
            print(p)


if __name__ == "__main__":
    main()
