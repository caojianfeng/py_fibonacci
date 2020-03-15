#!/usr/bin/env python3
LIMIT = 1474 #122.8年后，月数会超出这个数字，计算机也数不清有多少兔子了。


def fibos(month):
    fibo_list = []
    big = 0
    small = 1
    for i in range(0, min(month, LIMIT)):
        fibo_list.append({'month': i+1, 'small': small, 'big': big})
        big, small = small+big, big

    return fibo_list


def print_rabbits_fibos(fibos):
    print("|月份|小兔数量|大兔数量|")
    print("|:---:|:---:|:---:|")
    for fibo in fibos:
        print(f"|{fibo['month']}|{fibo['small']}|{fibo['big']}|")


if __name__ == "__main__":
    print_rabbits_fibos(fibos(12))
