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
    n = next_int()
    ar = sorted(next_int_array_one_line())
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ar[i] < ar[j] and ar[j] < ar[k] and ar[i] + ar[j] > ar[k]:
                    res += 1
    print(res)


if __name__ == '__main__':
    main()
