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
    s = next_line()
    x = 0
    if s == "RRR":
        x = 3
    elif s == "RRS" or s == "SRR":
        x = 2
    elif s == "SSS":
        x = 0
    else:
        x = 1
    print(x)


if __name__ == '__main__':
    main()
