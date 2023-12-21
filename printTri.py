# -*- coding: utf-8 -*-
# @Time : 2023/12/19 下午 04:11
# @Author : Zendo Chiu (segao)
# @Site :
# @File : printTri.py
# @Software: Pycharm


def pyramid(n):
    for i in range(n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


# 列印樹身
def pri(n, m):
    tempN = n
    tempM = m

    n = n * 2 + 1
    m = m * 2 + 1

    for x in range(n):
        if x % 2 == 1:
            Q = int((n - x) / 2)
            R = int((m - x) / 2)

            if tempN != tempM:
                for y in range(R):
                    print(" ", end="")
            else:
                for y in range(Q):
                    print(" ", end="")
            for t in range(x):
                print("^", end="")
            print("")


# 列印樹幹
def priTrunk(n):
    for x in range(n):
        if x != n - 1:
            print(" ", end="")
        else:
            print("*")
