#!/usr/bin/python
import math
import sys
LIMIT = 1474


def fibos(n):
    fibo_list = []
    last_step = 0
    this_step = 1
    for i in range(0, min(n, LIMIT)):
        fibo = this_step
        fibo_list.append(fibo)
        this_step, last_step = this_step+last_step, this_step
    return fibo_list


def print_fibos(n):
    index = 1
    fibo_list = fibos(n)
    for fibo in fibo_list:
        print("[%d]:%d" % (index, fibo))
        index += 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_fibos(10)
        exit(0)

    n = int(sys.argv[1])
    if n > LIMIT:
        print_fibos(LIMIT)
        print("Are you kidding me!Don`t bigger then %d" % LIMIT)
        exit(0)

    print_fibos(n)
