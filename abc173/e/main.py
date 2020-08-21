#!/usr/bin/env python3


def next_line():
    return input()


def next_int():
    return int(input())


def next_int_array_one_line():
    return list(map(int, input().split()))


def next_int_array_multi_lines(size):
    return [int(input()) for _ in range(size)]


def next_str_array(size):
    return [input() for _ in range(size)]


def main():
    n, k = map(int, input().split())
    ar = next_int_array_one_line()
    plus = []
    minus = []
    for i in range(n):
        if ar[i] >= 0:
            plus.append(ar[i])
        elif ar[i] < 0:
            minus.append(ar[i])
    use_p = 0
    use_m = 0
    size = 0
    res = 1
    plus = sorted(plus, key=lambda x: -abs(x))
    minus = sorted(minus, key=lambda x: -abs(x))
    while size < k:
        if use_p >= len(plus) - 1:


if __name__ == '__main__':
    main()
