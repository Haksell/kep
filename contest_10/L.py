# ruff: noqa: E731, E741
from itertools import accumulate, groupby
from operator import itemgetter
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    day_width, gap, start_week, events_number = mir()
    days = [[] for _ in range(5)]
    for i in range(events_number):
        start, finish = [int(x) - start_week for x in input().split()]
        assert start % 60 == finish % 60 == 0
        assert start // 86400 == finish // 86400
        assert start < finish
        days[start // 86400].append((start % 86400 // 60, finish % 86400 // 60, i))
    for day, slots in enumerate(days, 1):
        slots.sort(key=lambda t: (t[0], -t[1]))
        if day:
            print("=" * 80)
        print(day, len(slots))
        # events = []
        # for s, f, i in slots:
        #     events.append((s, True, i))
        #     events.append((f, False, i))
        # events.sort()
        # row = [(events[0][0], events[0][2], 0, 1)]
        # rows = [row]
        # starts = dict()
        # ends = dict()
        # for t, on, i in events[1:]:
        #     if not on:
        #         for _, j, start, end in row:
        #             starts[j] = start if j not in starts else max(start, starts[j])
        #             ends[j] = end if j not in ends else min(end, ends[j])
        #         row = [tup for tup in row if tup[1] != i]
        #     else:
        #         row = row.copy()
        #         for x, y in zip(row, row[1:]):
        #             if x[3] < y[2]:
        #                 row.append((t, i, x[3], y[2]))
        #                 break
        #         else:
        #             cp = []
        #             groups = [
        #                 (k, list(v))
        #                 for k, v in groupby(row, key=lambda tup: tup[1] in fixed)
        #             ]
        #             for i, (k, v) in enumerate(groups):
        #                 if k:
        #                     for e in v:
        #                         cp.append(e)
        #                 else:
        #                     start = 0 if i == 0 else cp[-1][3]
        #                     end = 1 if i == len(groups) - 1 else groups[i + 1][1][0][2]
        #                     for i, (a, b, c, d) in enumerate(v):
        #                         cp.append(
        #                             (
        #                                 a,
        #                                 b,
        #                                 start + i * (end - start) / len(v),
        #                                 start + (i + 1) * (end - start) / len(v),
        #                             )
        #                         )
        #             row = cp
        #             row.append((t, i, cp[-1][-1], 1))
        #     row.sort(key=itemgetter(2))
        #     rows.append(row)
        # print(*rows, sep="\n")
        # print(fixed)


if __name__ == "__main__":
    main()
