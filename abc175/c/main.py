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
    x, k, d = map(int, input().split())
    f = False
    if x < 0:
        f = True
        x = -x
    min_to_eq = x // d
    res = 0
    if min_to_eq >= k:
        # 同じ方向に動き続けるだけ
        res = x - d * k
    else:
        k -= min_to_eq
        x = x - d * min_to_eq
        if k % 2 != 0:
            res = x - d
        else:
            res = x
    if f:
        res = -res
    print(abs(res))


if __name__ == '__main__':
    main()
